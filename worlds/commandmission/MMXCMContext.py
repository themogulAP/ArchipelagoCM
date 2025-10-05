# Python related imports
import asyncio
import logging
import struct
from typing import Dict, Set

# AP related imports
import NetUtils
from CommonClient import CommonContext, logger
from worlds.tww.TWWClient import read_string

# 3rd party related imports
import dolphin_memory_engine as dolphin

# Project relative imports.
from .locations import LOCATION_TABLE
from .items import ALL_ITEMS_TABLE
from .MMXCMClient import MMXCMCommandProcessor
from .helpers import (CONNECTION_INITIAL_STATUS, CONNECTION_CONNECTED_STATUS, CONNECTION_REFUSED_STATUS,
    CONNECTION_LOST_STATUS, CLIENT_NAME, CONNECTION_VERIFY_SERVER, wait_for_next_loop)

# The functionality to add items, weapons, sub weapons, force metals, to our dynamic inventory.
# RAM addresses and the slot counts for each inventory type.
# The slot is 4 away from the previous one, and the data itself is a 4 Byte.
INVENTORY_INFO = {
    "Consumable": {
        "base_address": 0x804A32A9,
        "slot_count": 32,
        "slot_size": 4,
    },
    "Weapon": {
        "base_address": 0x804A34B9,
        "slot_count": 120,
        "slot_size": 4,
    },
    "Sub-Weapon": {
        "base_address": 0x804A3699,
        "slot_count": 64,
        "slot_size": 4,
    },
    "Force Metal": {
        "base_address": 0x804A3329,
        "slot_count": 96,
        "slot_size": 4,
    }
}

class MMXCMContext(CommonContext):
    """
    This is the context class for the Mega Man X: Command Mission client.
    This will inherit from the core class "CommonContext" in AP.
    This will hold all the game information, state, and functionality to run the client.
    """
    command_processor = MMXCMCommandProcessor
    game = "Mega Man X Command Mission"
    items_handling = 0b111
    dolphin_connected: bool = False
    seed_verified: bool = False
    already_fired_events = False
    game_running = False

    item_id_to_name: Dict[int, str]
    slot_to_player_name: Dict[int, str]

    dolphin_server_task = None
    dolphin_status = None
    medal_monitor_task: asyncio.Task = None # This manages the medal monitoring task async.

    logger = logging.getLogger(CLIENT_NAME)

    # Describing Constants for our Rebellion Medal Logic - - - - -
    SCREEN_SELECT_ADDRESS = 0x804A208B
    CUTSCENE_ID_ADDRESS = 0x804A208F
    ROOM_ID_ADDRESS = 0x804A2083

    REBELLION_MEDAL_CHECKS = { # These are the CUTSCENE IDs we want to tie to the Location.
        0x05: "Rebellion Medal 1", # Lagrano Ruins Clear
        0x12: "Rebellion Medal 2", # Central Tower Clear...
        0x1B: "Rebellion Medal 3",
        0x26: "Rebellion Medal 4",
        0x2D: "Rebellion Medal 5",
        0x37: "Rebellion Medal 6",
        0x3E: "Rebellion Medal 7",
        0x4A: "Rebellion Medal 8",
    }
    GRAVE_RUINS_MEDAL = "Rebellion Medal 9"

    def __init__(self, server_address, password):
        """
        Initialize the MMXCM Context
        :param server_address: Address of AP Server.
        :param password: Password for the server.
        """
        super().__init__(server_address, password)
        self.dolphin_status = CONNECTION_INITIAL_STATUS

    def run_gui(self):
        """Import kivy UI system from make_gui() and start running it as self.ui_task."""
        ui_class = self.make_gui()
        ui_class.base_title = CLIENT_NAME
        self.ui = ui_class(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def on_package(self, cmd: str, args: dict):
        """
        Handles the incoming network pakages from the server.
        """
        super().on_package(cmd, args)
        slot_data = args.get("slot_data", {})

        match cmd:
            case "Connected":

                # Seed verification step.
                arg_seed = str(slot_data["seed"])

                try:
                    # Read the ISO seed #
                    iso_seed = read_string(0x80000000, len(arg_seed))
                except Exception as genericEx:
                    iso_seed = ""
                    logger.error(str(genericEx))

                if arg_seed != iso_seed:
                    raise Exception("Error! Incorrect Randomized MMXCM Iso File. Seed does not match!")
                else:
                    self.seed_verified = True
                    logger.info("Game seed verified successfully")

                logger.info("Successfully connected to the Archipelago server!")
                self.game_running = True

            case "ReceivedItems":
                # This is the package sent when we get something from a different player.
                # We should call our own function to either update ram addresses or physically give items in game.
                pass

    async def disconnect(self, allow_autoreconnect: bool = False):
        await super().disconnect(allow_autoreconnect)

        if self.medal_monitor_task and not self.medal_monitor_task.done():
            self.medal_monitor_task.cancel()

        dolphin.un_hook()
        self.checked_locations = set()
        self.seed_verified = False
        self.dolphin_connected = False
        self.already_fired_events = False

    async def monitor_medals(self):
        """Monitors RAM addresses for Rebellion Medal completion and reports checks."""
        logger.info("Starting Rebellion Medal monitor...")
        new_checks_to_send: Set[int] = set()

        try:
            while not self.exit_event.is_set():
                # Use 'self' to access context properties
                if self.slot and dolphin.is_hooked():

                    # 1. Read the necessary memory addresses
                    # status_flag for Medals 1-8 check (must be 4)
                    status_flag = int.from_bytes(dolphin.read_bytes(self.SCREEN_SELECT_ADDRESS, 1), byteorder='big')
                    # cutscene_id for Medals 1-8 check (1-byte read)
                    cutscene_id = int.from_bytes(dolphin.read_bytes(self.CUTSCENE_ID_ADDRESS, 1), byteorder='big')

                    # room_id_value for Medal 9 check (2-byte read from dedicated address)
                    # Note: We must read as 2 bytes to get the full 1750 value (0x06D6)
                    room_id_value = int.from_bytes(dolphin.read_bytes(self.ROOM_ID_ADDRESS, 1), byteorder='big')

                    # --- CHECK LOGIC FOR MEDALS 1-8 (Status 4 + Unique 1-byte ID) ---
                    if status_flag == 0x04:
                        if cutscene_id in self.REBELLION_MEDAL_CHECKS:
                            location_name = self.REBELLION_MEDAL_CHECKS[cutscene_id]
                            # Use self.location_names_to_ids for lookup
                            medal_location_check_id = self.location_names.get(location_name)

                            if medal_location_check_id and medal_location_check_id not in self.checked_locations:
                                new_checks_to_send.add(medal_location_check_id)
                                self.checked_locations.add(medal_location_check_id)
                                logger.info(f"Medal check found: {location_name}")

                    # --- CHECK LOGIC FOR MEDAL 9 (Dedicated Room ID 1750) ---
                    medal_9_check_id = self.location_names.get(self.GRAVE_RUINS_MEDAL)

                    if room_id_value == 76:
                        if medal_9_check_id and medal_9_check_id not in self.checked_locations:
                            new_checks_to_send.add(medal_9_check_id)
                            self.checked_locations.add(medal_9_check_id)
                            logger.info(f"Medal check found: {self.GRAVE_RUINS_MEDAL}")

                    # --- REPORT NEW CHECKS ---
                    if new_checks_to_send:
                        # Use self.send_msgs to report the locations to the server
                        await self.send_msgs([{"cmd": "LocationChecks", "locations": list(new_checks_to_send)}])
                        new_checks_to_send.clear()

                await asyncio.sleep(3)  # Check every three seconds

        except Exception as e:
            logger.error(f"Error in Rebellion Medal monitor: {e}")
        finally:
            logger.info("Rebellion Medal monitor stopped.")

    async def game_watcher(self):
        """
        This is the main loop that will handle checking locations and giving items.
        It will run as long as the client is connected to the server.
        """
        # This initializes the set locations checked.
        checked_locations_in_game = set()

        # This will track the medals we have reported.
        reported_medals = set()

        while not self.finished_game:
            # Check for new locations.
            # Replace these with the flags in locations py.
            newly_checked_locations = []
            for location_name, location_info in LOCATION_TABLE.items():
                if location_name not in checked_locations_in_game:
                    # Sets ram _data to default none to avoid the errors.
                    ram_data = None
                    # Reads the value at the locations RAM address.
                    try:
                        ram_data = location_info.ram_addr
                        if ram_data:
                            # Read the value at the locations RAM address.
                            location_value = dolphin.read_bytes(ram_data.ram_addr, 1)[0]
                            # Check if the location's bit position has been set in the value.
                            if (location_value & (1 << ram_data.bit_position)) > 0:
                                newly_checked_locations.append(location_name)
                                checked_locations_in_game.add(location_name)
                    except Exception as e:
                        logger.error(
                            f"Error reading location '{location_name}' at address {hex(ram_data.ram_addr)}: {e}")

            if newly_checked_locations:
                print(f"Found new locations: {newly_checked_locations}")
                await self.check_locations(newly_checked_locations)

            if not self.finished_game:
                try:
                    # Get the RAM data for the Great Redips event. This is our "beating the game".
                    redips_ram_data = LOCATION_TABLE["Defeated Great Redips"].ram_addr

                    if redips_ram_data:
                        # Read the value at the event's memory address.
                        boss_defeated_value = dolphin.read_bytes(redips_ram_data.ram_addr, 1)[0]

                        # Check if the bit for defeating Redips is set.
                        if boss_defeated_value == 9:
                            print("Final boss defeated! Signaling game completion to the server.")
                            self.finished_game = True  # This ends the while loop on the next pass.
                            await self.send_msgs([{
                                "cmd": "StatusUpdate",
                                "status": NetUtils.ClientStatus.CLIENT_GOAL,
                            }])
                except Exception as e:
                    # This will catch errors if the game state is not readable or the address is invalid.
                    logger.error(f"Error checking for game completion: {e}")

            # Check for new items.
            while self.items_received:
                item_to_add = self.items_received.pop(0)

                item_name = self.item_id_to_name[item_to_add.item]
                player_name = self.slot_to_player_name[item_to_add.player]
                print(f"Received item: {item_name} from {player_name}.")

                # ---------------------- Dynamic LOGIC for all Access Codes to change the RAM addresses once received. ---------------------------
                # Lagrano Ruins
                if item_name == "Lagrano Ruins Access Code":
                    print("Lagrano Access Code received! Patching RAM to enable the teleporter.")
                    try:
                        # Write the first PowerPC instruction.
                        dolphin.write_bytes(0x80082fa4, b'\x3c\x80\x00\x01')

                        # Write the second PowerPC instruction.
                        dolphin.write_bytes(0x80082fac, b'\x38\x08\x03\x46')

                    except Exception as e:
                        logger.error(f"Error while writing to RAM for Lagrano Access Code: {e}")

                    # We do not want to add this to the in-game inventory, so we skip the rest of the loop.
                    continue

                # Central Tower: Changing the Spider , Arakure, and Aile Blockers.
                elif item_name == "Central Tower Access Code":
                    print("Central Tower Access Code received! Changing RAM value to enable the teleporter.")
                    try:
                        # Write a single byte with a value of 0 -  removes cutscene blockers.
                        dolphin.write_bytes(0x804A20BD, b'\x00')

                        # Write a single byte with a value of 1 - removes Aile Blocker
                        dolphin.write_bytes(0x804A20C1, b'\x01')

                    except Exception as e:
                        logger.error(f"Error while writing to RAM for Central Tower Access Code: {e}")

                    continue

                # Tianna Camp
                elif item_name == "Tianna Camp Access Code":
                    print("Tianna Camp Access Code received! Patching RAM to enable the teleporter.")
                    try:
                        # Write the first PowerPC instruction.
                        dolphin.write_bytes(0x80082fcc, b'\x3c\x80\x00\x03')

                        # Write the second PowerPC instruction.
                        dolphin.write_bytes(0x80082fd4, b'\x38\x04\x01\x41')

                    except Exception as e:
                        logger.error(f"Error while writing to RAM for Tianna Camp Access Code: {e}")

                    # We do not want to add this to the in-game inventory, so we skip the rest of the loop.
                    continue

                # Gaudile Laboratory Teleport
                elif item_name == "Gaudile Laboratory Access Code":
                    print("Gaudile Laboratory Access Code received! Patching RAM to enable the teleporter.")
                    try:
                        # Write the first PowerPC instruction.
                        dolphin.write_bytes(0x80082ff4, b'\x3c\x80\x00\x04')

                        # Write the second PowerPC instruction.
                        dolphin.write_bytes(0x80082ffC, b'\x38\x04\x01\x41')

                    except Exception as e:
                        logger.error(f"Error while writing to RAM for Gaudile Laboratory Access Code: {e}")

                    continue

                # Ulfat Factory Access Code
                elif item_name == "Ulfat Factory Access Code":
                    print("Ulfat Factory Access Code received! Patching RAM to enable the teleporter.")
                    try:
                        # Write the first PowerPC instruction.
                        dolphin.write_bytes(0x8008301c, b'\x3c\x80\x00\x05')

                        # Write the second PowerPC instruction.
                        dolphin.write_bytes(0x80083024, b'\x38\x04\x01\x41')

                    except Exception as e:
                        logger.error(f"Error while writing to RAM for Ulfat Factory Access Code: {e}")

                    continue

                # Gimialla Mine
                elif item_name == "Gimialla Mine Access Code":
                    print("Gimialla Mine Access Code received! Patching RAM to enable the teleporter.")
                    try:
                        # Write the first PowerPC instruction.
                        dolphin.write_bytes(0x80083044, b'\x3c\x80\x00\x06')

                        # Write the second PowerPC instruction.
                        dolphin.write_bytes(0x8008304c, b'\x38\x04\x01\x41')

                    except Exception as e:
                        logger.error(f"Error while writing to RAM for Gimialla Mine Access Code: {e}")

                    continue

                # Vanallia Desert
                elif item_name == "Vanallia Desert Access Code":
                    print("Vanallia Desert Access Code received! Patching RAM to enable the teleporter.")
                    try:
                        # Write the first PowerPC instruction.
                        dolphin.write_bytes(0x8008306c, b'\x3c\x80\x00\x07')

                        # Write the second PowerPC instruction.
                        dolphin.write_bytes(0x80083074, b'\x38\x04\x01\x41')

                    except Exception as e:
                        logger.error(f"Error while writing to RAM for Vanallia Desert Access Code: {e}")

                    continue

                # Melda Ore Plant ----------------
                elif item_name == "Melda Ore Plant Access Code":
                    print("Melda Ore Plant Access Code received! Patching RAM to enable the teleporter.")
                    try:
                        # Write the first PowerPC instruction.
                        dolphin.write_bytes(0x80083094, b'\x3c\x80\x00\x08')

                        # Write the second PowerPC instruction.
                        dolphin.write_bytes(0x8008309c, b'\x38\x04\x01\x41')

                    except Exception as e:
                        logger.error(f"Error while writing to RAM for Melda Ore Plant Access Code: {e}")

                    continue

                elif item_name == "Grave Ruins Base Access Code":
                    print("Grave Ruins Base Access Code received! Patching RAM to enable the teleporter.")
                    try:
                        # Write the first PowerPC instruction.
                        dolphin.write_bytes(0x800830bc, b'\x3c\x80\x00\x09')

                        # Write the second PowerPC instruction.
                        dolphin.write_bytes(0x800830c4, b'\x38\x04\x01\x41')

                    except Exception as e:
                        logger.error(f"Error while writing to RAM for Grave Ruins Base Access Code: {e}")

                    continue
                # --- ---------------------------END DYNAMIC CLIENT LOGIC ------------------------------------------------------

                item_info = ALL_ITEMS_TABLE.get(item_name)

                if item_info and "type" in item_info:
                    item_type = item_info["type"]
                    await self.write_to_inventory(item_to_add, item_type)
                else:
                    logger.error(f"Error: Could not find type information for item ID {item_to_add.item}.")

            await asyncio.sleep(1)  # Can set this so sleep to avoid CPU usage.

        print("Disconnected from Dolphin.")

    # Starts the full loop and debug messages for connecting to Dolphin.
    async def dolphin_connect_loop(self):
        """
        Connects to the Dolphin emulator and waits for the correct game to be running.
        """
        while not self.exit_event.is_set():
            try:
                if not dolphin.is_hooked():
                    dolphin.hook()
                    if dolphin.get_status() == dolphin.get_status().noEmu or dolphin.get_status() == dolphin.get_status().notRunning:
                        dolphin.un_hook()
                    self.dolphin_status = CONNECTION_INITIAL_STATUS
                    logger.info(self.dolphin_status)
                    await wait_for_next_loop(5)
                    continue

                # If the Game ID is a standard one, disconnect because it isnt the randomized ROM.
                if not self.dolphin_status == CONNECTION_CONNECTED_STATUS:
                    game_id = read_string(0x80000000, 6)
                    if game_id in ["GXRP08"]:
                        logger.info(CONNECTION_REFUSED_STATUS)
                        self.dolphin_status = CONNECTION_REFUSED_STATUS
                        dolphin.un_hook()
                        await wait_for_next_loop(5)
                        continue

                self.locations_checked = set()

                # Inform player we are ready for connection
                if not self.dolphin_status == CONNECTION_VERIFY_SERVER:
                    self.dolphin_status = CONNECTION_VERIFY_SERVER
                    logger.info(self.dolphin_status)
                await self.server_auth()

                if not self.slot:
                    await wait_for_next_loop(5)
                    continue

                if not self.medal_monitor_task or self.medal_monitor_task.done():
                    self.medal_monitor_task = asyncio.create_task(self.monitor_medals(), name= "MMXCM Medal Monitor")

            except Exception as genericEx:
                dolphin.un_hook()
                logger.error(str(genericEx))
                logger.info("Connection to Dolphin failed, attempting in 5 seconds...")
                self.dolphin_status = CONNECTION_LOST_STATUS
                await self.disconnect()
                await asyncio.sleep(5)
                continue

    async def write_to_inventory(self, item: NetUtils.NetworkItem, inv_type: str):
        """
        This will find the first empty inventory slot and write the item's ID to it.
        """
        # Look up the item's data using its name, not its Archipelago ID
        item_info = ALL_ITEMS_TABLE.get(self.item_id_to_name[item.item])

        if not item_info:
            logger.error(f"Error: Could not find item information for item ID {item.item}.")
            return

        if inv_type not in INVENTORY_INFO:
            logger.error(f"Error Unknown inventory type '{inv_type}' for item {self.item_id_to_name[item.item]}.")
            return

        inv_data = INVENTORY_INFO[inv_type]
        base_address = inv_data["base_address"]
        slot_count = inv_data["slot_count"]
        slot_size = inv_data["slot_size"]

        for i in range(slot_count):
            slot_address = base_address + (i * slot_size)

            # Reads the current value of the slot
            current_item_id_bytes = dolphin.read_bytes(slot_address, slot_size)
            current_item_id = struct.unpack(">I", current_item_id_bytes)[0]

            # A Value of 0 indicates an empty slot!
            if current_item_id == 0:
                print(f"Found empty {inv_type} slot at address {hex(slot_address)}")

                # Get the in-game Item ID and convert it to bytes.
                item_id_bytes = struct.pack(">I", item_info["item_id"])

                # Write the item to the empty slot.
                dolphin.write_bytes(slot_address, item_id_bytes)
                print(f"Wrote item {self.item_id_to_name[item.item]} ({item.item}) to {inv_type} inventory.")
                return  # Exit after writing the item to the inventory slot.
        logger.error(f"Error: No empty {inv_type} slots found for item {item.item}!")