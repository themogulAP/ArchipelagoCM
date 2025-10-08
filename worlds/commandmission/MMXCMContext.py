# Python related imports
import asyncio
import copy
import logging
import struct
from typing import Dict, Set

# AP related imports
import NetUtils
from CommonClient import CommonContext, logger
from worlds.tww.TWWClient import read_string

# 3rd party related imports
import dolphin_memory_engine as dolphin

from .files.Constants import WAIT_TIMER_SHORT_TIMEOUT
# Project relative imports.
from .locations import LOCATION_TABLE
from .items import ALL_ITEMS_TABLE
from .MMXCMClient import MMXCMCommandProcessor
from .helpers import *
from .files.patch_codes import ACCESS_CODE_PATCHES
from .files import Constants

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

# These addresses appear to be unused throughout the game - we will use them for Item get refactoring.
LAST_RECV_ITEM_ADDR = 0x804A2174
NOT_SAVE_LAST_RECV_ITEM_ADDR = 0x804A2175

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

    item_id_to_name: Dict[int, str] = {}
    slot_to_player_name: Dict[int, str] = {}

    dolphin_server_task = None
    dolphin_status = None
    medal_monitor_task: asyncio.Task = None # This manages the medal monitoring task async.
    revert_monitor_task: asyncio.Task = None # Task for Reverting the Big 4 (monitoring)

    logger = logging.getLogger(CLIENT_NAME)

    Constants = Constants

    def __init__(self, server_address, password):
        """
        Initialize the MMXCM Context
        :param server_address: Address of AP Server.
        :param password: Password for the server.
        """
        super().__init__(server_address, password)
        self.dolphin_status = CONNECTION_INITIAL_STATUS
        self.arg_seed = ""

        self.last_received_idx: int = 0
        self.non_save_last_recv_idx: int = 0

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
                self.arg_seed = str(slot_data["seed"])
                self.game_running = True

            case "ReceivedItems":
                # This is the package sent when we get something from a different player.
                # We should call our own function to either update ram addresses or physically give items in game.
                pass

    async def disconnect(self, allow_autoreconnect: bool = False):
        await super().disconnect(allow_autoreconnect)

        if self.medal_monitor_task and not self.medal_monitor_task.done():
            self.medal_monitor_task.cancel()

        if self.revert_monitor_task and not self.revert_monitor_task.done():
            self.revert_monitor_task.cancel()

        dolphin.un_hook()
        self.checked_locations = set()
        self.seed_verified = False
        self.dolphin_connected = False
        self.already_fired_events = False

    def apply_big_4(self, is_medal_2: bool):
        """Applies the four required PowerPC patches, using a unique 4th patch for Medal 2."""
        # Determine which unique 4th patch to use
        patch_4_value = self.Constants.HELIPAD_PATCH if is_medal_2 else self.Constants.ARCADE_PATCH
        patch_name = "Helipad" if is_medal_2 else "Arcade"

        logger.info(f"APPLYING The Big 4 PowerPC patches ({patch_name}).")
        try:
            # Shared Patches (1, 2, 3)
            dolphin.write_bytes(self.Constants.GAMEPLAY_STATE_SET_ADDR, self.Constants.GAMEPLAY_PATCH)
            dolphin.write_bytes(self.Constants.GAMEPLAY_STATE_STORE_ADDR, self.Constants.GAMEPLAY_STORE_PATCH)
            dolphin.write_bytes(self.Constants.STAGE_SET_ADDR, self.Constants.STAGE_PATCH)
            # Unique/Common Patch (4)
            dolphin.write_bytes(self.Constants.AREA_SET_ADDR, patch_4_value)
        except Exception as e:
            logger.error(f"Error applying 'Big 4' patches ({patch_name}): {e}")

    def revert_big_4(self):
        """Reverts the four required PowerPC patches back to their original state."""
        logger.info("REVERTING The Big 4 PowerPC patches.")
        try:
            dolphin.write_bytes(self.Constants.GAMEPLAY_STATE_SET_ADDR, self.Constants.GAMEPLAY_SET_VANILLA)
            dolphin.write_bytes(self.Constants.GAMEPLAY_STATE_STORE_ADDR, self.Constants.GAMEPLAY_STORE_VANILLA)
            dolphin.write_bytes(self.Constants.STAGE_SET_ADDR, self.Constants.STAGE_VANILLA)
            dolphin.write_bytes(self.Constants.AREA_SET_ADDR, self.Constants.AREA_VANILLA)
        except Exception as e:
            logger.error(f"Error reverting 'Big 4' patches: {e}")

    async def monitor_revert_state(self):
        """Monitors RAM conditions to trigger the revert of the Big 4 PowerPC patches."""
        logger.info("Starting Big 4 revert monitor...")

        try:
            if self.slot and dolphin.is_hooked():

                # Read the two addresses necessary for all revert conditions
                # REVERT_STATE_ADDRESS (0x804A208E) is used for values 4 and 20
                revert_state_value = int.from_bytes(
                    dolphin.read_bytes(self.Constants.REVERT_STATE_ADDRESS, 1), byteorder='big'
                )

                # SCREEN_SELECT_ADDRESS (0x804A208B) is used for values 5 and 7
                screen_select_value = int.from_bytes(
                    dolphin.read_bytes(self.Constants.SCREEN_SELECT_ADDRESS, 1), byteorder='big'
                )

                # --- Evaluate Conditions ---

                # All three Arcade/Helipad reverts require the game to be in state 7 (exiting room)
                is_game_state_7 = (screen_select_value == 7)

                # Condition 3 (Exit 3) requires SCREEN_SELECT = 5 (without game state 7 check)
                is_exit_3 = (screen_select_value == 5)

                # Condition 4 (Medal 2-specific revert) requires REVERT_STATE = 20 AND SCREEN_SELECT = 7
                is_medal_2_revert = (revert_state_value == 20) and is_game_state_7

                # Conditions 1 & 2 (Arcade reverts) require REVERT_STATE = 4 AND SCREEN_SELECT = 7
                is_arcade_revert = (revert_state_value == 4) and is_game_state_7

                # --- Trigger Revert if ANY condition is met ---
                if is_exit_3 or is_medal_2_revert or is_arcade_revert:
                    # Revert the patches and break the loop to end the monitoring task
                    self.revert_big_4()

        except Exception as e:
            logger.error(f"Error in Big 4 revert monitor: {e}")
        finally:
            logger.info("Big 4 revert monitor stopped.")

    async def monitor_medals(self):
        """Monitors RAM addresses for Rebellion Medal completion and reports checks."""
        #logger.info("Starting Rebellion Medal monitor...")
        # Use 'self' to access context properties
        # 1. Read the necessary memory addresses
        # status_flag for Medals 1-8 check (must be 4)
        status_flag = int.from_bytes(dolphin.read_bytes(self.Constants.SCREEN_SELECT_ADDRESS, 1), byteorder='big')
        # cutscene_id for Medals 1-8 check (1-byte read)
        cutscene_id = int.from_bytes(dolphin.read_bytes(self.Constants.CUTSCENE_ID_ADDRESS, 1), byteorder='big')

        # room_id_value for Medal 9 check (1-byte read from dedicated address)
        # Note: We must read as 1 byte to get the full 76 Room value (0x4C)
        room_id_value = int.from_bytes(dolphin.read_bytes(self.Constants.ROOM_ID_ADDRESS, 1), byteorder='big')

        # --- CHECK LOGIC FOR MEDALS 1-8 (Status 4 + Unique 1-byte ID) ---
        if status_flag == 0x04: # This is for the Cutscene Screen State.
            if cutscene_id in self.Constants.REBELLION_MEDAL_CHECKS:
                # TODO: UPDATE THE THREE CONSTANT PATCHES FOR MEDALS TO TELEPORT TO ARCADE OR HELIPAD.
                pass
        # --- CHECK LOGIC FOR MEDAL 9 (Dedicated Room ID 1750) ---

        if room_id_value == 76:
            # TODO: Check self.items_received contains medal 9. Then teleport back to Arcade.
            pass

        await asyncio.sleep(3)  # Check every three seconds

    def update_received_idx(self, last_recov_idx: int):
        """
        This will write the current item index to saveable and non saveable RAM address using 4 byte write,
        to overall prevent the player from getting EVERY check every time they login.
        """
        self.last_received_idx = last_recov_idx

        byte_data = last_recov_idx.to_bytes(4, 'big')

        try:
            dolphin.write_bytes(LAST_RECV_ITEM_ADDR, byte_data)
        except Exception as e:
            logger.info(f"Error writing 4-byte index to LAST RECOV ITEM ADDR: {e}")

        if last_recov_idx > self.non_save_last_recv_idx:
            self.non_save_last_recv_idx = last_recov_idx
            try:
                dolphin.write_bytes(NOT_SAVE_LAST_RECV_ITEM_ADDR, byte_data)
            except Exception as e:
                logger.info(f"Error writing 4-byte index to NOT SAVE LAST RECOV ITEM.")

    async def game_watcher(self):
        """
        This is the main loop that will handle checking locations and giving items.
        It will run as long as the client is connected to the server.
        """
        #logger.info("Starting Location check Loop!")
        # Check for new locations.
        # Missing locations is the AP ID , a list of integers broken down by AP.
        local_missing_locations = copy.deepcopy(self.missing_locations) # Deepcopy makes it separate copies.
        for missing_locations in local_missing_locations: #Missing locations is the value from for loop.
            logger.info("Line 263")
            local_location_name = self.location_names.lookup_in_game(missing_locations)
            mmxcm_local_data = LOCATION_TABLE[local_location_name] #This grabs the data per name from AP ID.
            # Read the value at the locations RAM address.
            location_value = dolphin.read_bytes(mmxcm_local_data.ram_data.ram_addr, 1)[0]
            logger.info("Line 268")
            # Check if the location's bit position has been set in the value.
            if (location_value & (1 << mmxcm_local_data.ram_data.bit_position)) > 0:
                self.locations_checked.add(missing_locations)
        #logger.info("Ending Location check Loop!")
        logger.info("Line 268")
        await self.check_locations(self.locations_checked) # Locations_checked = LOCAL locations of game
        # Checked_locations = AP SERVER STATE of locations.

        if not self.finished_game:
            #logger.info("Checking finished game!")
            try:
                logger.info("Line 280")
                # Get the RAM data for the Great Redips event. This is our "beating the game".
                redips_ram_data = LOCATION_TABLE["Defeated Great Redips"].ram_data

                if redips_ram_data:
                    logger.info("Line 285")
                    # Read the value at the event's memory address.
                    boss_defeated_value = dolphin.read_bytes(redips_ram_data.ram_addr, 1)[0]

                    # Check if the bit for defeating Redips is set.
                    if boss_defeated_value == 9:
                        logger.info("Line 291")
                        print("Final boss defeated! Signaling game completion to the server.")
                        self.finished_game = True  # This ends the while loop on the next pass.
                        await self.send_msgs([{
                            "cmd": "StatusUpdate",
                            "status": NetUtils.ClientStatus.CLIENT_GOAL,
                        }])
                        logger.info("Line 298")
            except Exception as e:
                # This will catch errors if the game state is not readable or the address is invalid.
                logger.error(f"Error checking for game completion: {e}")

        # Check for new items.
          #  logger.info("Starting Received Items Loop- Index Based!")
            # TODO: Refactor this to the LAST SAVED IDX (Based on LM's code) FIRST, WE NEED THE FULL 4 BLOCK STILL
            # Add function for Far East HQ bit position door for chpt 10 upon receiving 9 Medals and FE HQ Code.

            # 1 --- -- Read the Saveable Index from RAM ------
            try:
                logger.info("Line 310")
                # Read the 4 bytes from defined Saveable RAM address.
                ram_bytes = dolphin.read_bytes(LAST_RECV_ITEM_ADDR, 4)
                last_recv_idx = int.from_bytes(ram_bytes, 'big')
            except Exception as e:
                logger.info("Line 315")
                logger.warning(f"Failed to read saveable index from RAM: {e}")
                last_recv_idx = 0

            # 2 - - - - -Compare the saved index to the total number received from AP server.
            if len(self.items_received) == last_recv_idx:
                #logger.info("No New Items received since last save.")
                #logger.info("Ending Received Items Loop!")
                logger.info("Line 323")
                return

            # 3 - - -  - Read Non-Saveable Index (for future use on traps and such)
            self.last_received_idx = last_recv_idx
            try:
                logger.info("Line 329")
                non_save_bytes = dolphin.read_bytes(NOT_SAVE_LAST_RECV_ITEM_ADDR, 4)
                self.non_save_last_recv_idx = int.from_bytes(non_save_bytes, 'big')
            except Exception as e:
                logger.warning(f"Failed to read non-saveable index from RAM: {e}")
                self.non_save_last_recv_idx = 0

            # 4 -  - - Get ONLY the new items received from the AP server since our last saved index.
            recv_items = self.items_received[last_recv_idx:]

            # 5 -  - - Process EACH new item! - - - -
            for item_to_add in recv_items:
                logger.info("Line 341")
                last_recv_idx += 1

                # - Get the readable names
                item_name = self.item_id_to_name[item_to_add.item]
                player_name = self.slot_to_player_name[item_to_add.player]

                print(f"Received item: {item_name} from {player_name}.")

                # Check for Rebellion Medals
                if item_name.startswith("Rebellion Medal"):
                    logger.info("Line 352")
                    #Determine if its Jango's Medal
                    is_medal_2 = (item_name == "Rebellion Medal 2")
                    self.apply_big_4(is_medal_2)

                    #After patch is applied, we need to start the monitoring
                    #This will eventually revert the changes.
                    if not self.revert_monitor_task or self.revert_monitor_task.done():
                        self.revert_monitor_task = asyncio.create_task(
                            self.monitor_revert_state(),
                            name="Revert Monitor"
                    )

                    self.update_received_idx(last_recv_idx)
                    logger.info("Line 366")
                    continue

                # Dynamic LOGIC for all Access Codes to change the RAM addresses once received.
                if item_name in ACCESS_CODE_PATCHES:
                    try:
                        logger.info("Line 372")
                        # Call the patching function and execute it from our new patch codes py
                        ACCESS_CODE_PATCHES[item_name]()
                    except Exception as e:
                        logger.error(f" Error while writing RAM for {item_name}: {e}")

                    self.update_received_idx(last_recv_idx)
                    continue
                # END DYNAMIC CLIENT LOGIC

                item_info = ALL_ITEMS_TABLE.get(item_name)

                if item_info and "type" in item_info:
                    logger.info("Line 385")
                    item_type = item_info["type"]
                    await self.write_to_inventory(item_to_add, item_type)
                    self.update_received_idx(last_recv_idx)
                    logger.info("Line 389")
                else:
                    logger.error(f"Error: Could not find type information for item ID {item_to_add.item}.")
           # logger.info("Ending Received Items Loop!")

    async def server_auth(self, password_requested: bool = False):
        """
        Authenticate with the Archipelago server.

        :param password_requested: Whether the server requires a password. Defaults to `False`.
        """
        if password_requested and not self.password:
            await super(MMXCMContext, self).server_auth(password_requested)
        if self.dolphin_status != CONNECTION_VERIFY_SERVER:
            return
        if not self.auth:
            await self.get_username()
        await self.send_connect()

        if self.slot:
            logger.info(CONNECTION_CONNECTED_STATUS)
            self.dolphin_status = CONNECTION_CONNECTED_STATUS

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

                    arg_seed = read_string(0x80000001, len(str(self.arg_seed)))
                    if arg_seed != self.arg_seed:
                        raise Exception(
                            "Incorrect Randomized MMX Command Mission ISO file selected. The seed does not match." +
                            "Please verify that you are using the right ISO/seed/apmmxcm file.")

                await self.game_watcher()
                await self.monitor_medals()
                await wait_for_next_loop(WAIT_TIMER_SHORT_TIMEOUT)

            except Exception as genericEx:
                dolphin.un_hook()
                logger.error("Generic Exception hit while in Dolphin Connect Loop. Additional details: " +str(genericEx))
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