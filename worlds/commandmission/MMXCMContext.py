# Python related imports
import asyncio
import copy
import logging
import struct
from typing import Dict, Set, TYPE_CHECKING

# AP related imports
import NetUtils
from CommonClient import CommonContext, logger
from worlds.tww.TWWClient import read_string

# 3rd party related imports
import dolphin_memory_engine as dolphin

from .files.Constants import WAIT_TIMER_SHORT_TIMEOUT
# Project relative imports.
from .locations import LOCATION_TABLE
from .items import ALL_ITEMS_TABLE, MMXCMItemData
from .MMXCMClient import MMXCMCommandProcessor
from .helpers import *
from .files.patch_codes import ACCESS_CODE_PATCHES
from .files import Constants

# The functionality to add items, weapons, sub weapons, force metals, to our dynamic inventory.
# RAM addresses and the slot counts for each inventory type.
# The slot is 4 away from the previous one, and the data itself is a 4 Byte.
INVENTORY_INFO = {
    "Consumable": {
        "base_address": 0x804A32A8,
        "slot_count": 32,
        "slot_size": 4,
    },
    "Weapon": {
        "base_address": 0x804A34B8,
        "slot_count": 120,
        "slot_size": 4,
    },
    "Sub-Weapon": {
        "base_address": 0x804A3698,
        "slot_count": 64,
        "slot_size": 4,
    },
    "Force Metal": {
        "base_address": 0x804A3328,
        "slot_count": 96,
        "slot_size": 4,
    }
}

# These addresses appear to be unused throughout the game - we will use them for Item get refactoring.
LAST_RECV_ITEM_ADDR = 0x804A2174
NOT_SAVE_LAST_RECV_ITEM_ADDR = 0x804A2175

# This is the address that holds the player's slot name.
# This way, the player does not have to manually authenticate their slot name.
SLOT_NAME_ADDR = 0x802E3D00
SLOT_NAME_STR_LENGTH = 64

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
        logger.info("Starting Rebellion Medal monitor...")

        # Use 'self' to access context properties
        # 1. Read the necessary memory addresses
        # status_flag for Medals 1-8 check (must be 4)
        status_flag = int.from_bytes(dolphin.read_bytes(self.Constants.SCREEN_SELECT_ADDRESS, 1), byteorder='big')
        # cutscene_id for Medals 1-8 check (1-byte read)
        cutscene_id = int.from_bytes(dolphin.read_bytes(self.Constants.CUTSCENE_ID_ADDRESS, 1), byteorder='big')

        # --- CHECK LOGIC FOR MEDALS 1-8 (Status 4 + Unique 1-byte ID) ---
        if status_flag == 0x04: # This is for the Cutscene Screen State.
            if cutscene_id in self.Constants.REBELLION_MEDAL_CHECKS:
                # TODO: UPDATE THE THREE CONSTANT PATCHES FOR MEDALS TO TELEPORT TO ARCADE OR HELIPAD.
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

    async def write_bytes_and_validate(self, addr: int, ram_offset: list[str] | None, curr_value: bytes) -> None:
        if not ram_offset:
            dolphin.write_bytes(addr, curr_value)
        else:
            dolphin.write_bytes(dolphin.follow_pointers(addr, ram_offset), curr_value)

    def check_ingame(self):
        # The game has an address that lets us know if we are in a playable state or not.
        int_play_state = dolphin.read_byte(self.Constants.SCREEN_SELECT_ADDRESS)
        if not int_play_state == 7:
            return False
        return True

    async def game_watcher(self):
        """
        This is the main loop that will handle checking locations and giving items.
        It will run as long as the client is connected to the server.
        """
        # This will check for the game state being 7 to make sure the player is in game.
        if not self.check_ingame():
            return

        #logger.info("Starting Location check Loop!")
        # Check for new locations.
        # Missing locations is the AP ID , a list of integers broken down by AP.
        local_missing_locations = copy.deepcopy(self.missing_locations) # Deepcopy makes it separate copies.
        for missing_locations in local_missing_locations: #Missing locations is the value from for loop.
            local_location_name = self.location_names.lookup_in_game(missing_locations)
            mmxcm_local_data = LOCATION_TABLE[local_location_name] #This grabs the data per name from AP ID.
            # Read the value at the locations RAM address.
            location_value: int = dolphin.read_byte(mmxcm_local_data.ram_data.ram_addr)
            # Check if the location's bit position has been set in the value.
            if (location_value & (1 << mmxcm_local_data.ram_data.bit_position)) > 0:
                self.locations_checked.add(missing_locations)
        #logger.info("Ending Location check Loop!")
        await self.check_locations(self.locations_checked) # Locations_checked = LOCAL locations of game
        # Checked_locations = AP SERVER STATE of locations.

        if not self.finished_game:
            #logger.info("Checking finished game!")
            try:
                # Get the RAM data for the Great Redips event. This is our "beating the game".
                redips_ram_data = LOCATION_TABLE["Defeated Great Redips"].ram_data

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
            # Add function for Far East HQ bit position door for chpt 10 upon receiving 9 Medals and FE HQ Code.

            # 1 --- -- Read the Saveable Index from RAM ------
            try:
                # Read the 4 bytes from defined Saveable RAM address.
                ram_bytes = dolphin.read_bytes(LAST_RECV_ITEM_ADDR, 4)
                last_recv_idx = int.from_bytes(ram_bytes, 'big')
            except Exception as e:
                logger.warning(f"Failed to read saveable index from RAM: {e}")
                last_recv_idx = 0

            # 2 - - - - -Compare the saved index to the total number received from AP server.
            if len(self.items_received) == last_recv_idx:
                #logger.info("No New Items received since last save.")
                #logger.info("Ending Received Items Loop!")
                return

            # 3 - - -  - Read Non-Saveable Index (for future use on traps and such)
            self.last_received_idx = last_recv_idx
            try:
                non_save_bytes = dolphin.read_bytes(NOT_SAVE_LAST_RECV_ITEM_ADDR, 4)
                self.non_save_last_recv_idx = int.from_bytes(non_save_bytes, 'big')
            except Exception as e:
                logger.warning(f"Failed to read non-saveable index from RAM: {e}")
                self.non_save_last_recv_idx = 0

            # 4 -  - - Get ONLY the new items received from the AP server since our last saved index.
            recv_items = self.items_received[last_recv_idx:]

            # 5 -  - - Process EACH new item! - - - -
            for item_to_add in recv_items:
                last_recv_idx += 1

                # - Get the readable names
                item_name = self.item_names.lookup_in_game(item_to_add.item)
                item_info = ALL_ITEMS_TABLE.get(item_name)
                item_type = item_info.type

                # Check for Rebellion Medals
                if item_name.startswith("Rebellion Medal"):
                    #Determine if its Jango's Medal
                    is_medal_2 = (item_name == "Rebellion Medal 2")
                    self.apply_big_4(is_medal_2)

                    #After patch is applied, we need to start the monitoring
                    #This will eventually revert the changes.
                    # if not self.revert_monitor_task or self.revert_monitor_task.done():
                    #     self.revert_monitor_task = asyncio.create_task(
                    #         self.monitor_revert_state(),
                    #         name="Revert Monitor"
                    # )
                    await self.monitor_revert_state()

                    self.update_received_idx(last_recv_idx)
                    continue

                # Dynamic LOGIC for all Access Codes to change the RAM addresses once received.
                elif item_name in ACCESS_CODE_PATCHES:
                    try:
                        # Call the patching function and execute it from our new patch codes py
                        ACCESS_CODE_PATCHES[item_name]()
                    except Exception as e:
                        logger.error(f" Error while writing RAM for {item_name}: {e}")

                    self.update_received_idx(last_recv_idx)
                    continue

                elif item_type == "Mechaniloid Item" or item_type == "Trade Item" or item_type == "Major Item" or item_type == "Key Item":
                    for addr_to_update in item_info.update_ram_addr:
                        byte_size = 1 if addr_to_update.ram_byte_size is None else addr_to_update.ram_byte_size
                        ram_offset = None if not addr_to_update.pointer_offset else [addr_to_update.pointer_offset]

                        if not addr_to_update.item_count is None:
                            if not ram_offset is None:
                                curr_val = int.from_bytes(dolphin.read_bytes(dolphin.follow_pointers(addr_to_update.ram_addr,
                                        [addr_to_update.pointer_offset]), byte_size))

                                curr_val += addr_to_update.item_count
                            else:
                                curr_val = int.from_bytes(dolphin.read_bytes(addr_to_update.ram_addr, byte_size))
                                curr_val += addr_to_update.item_count
                        else:
                            if not addr_to_update.pointer_offset is None:
                                curr_val = int.from_bytes(dolphin.read_bytes(dolphin.follow_pointers(addr_to_update.ram_addr,
                                    [addr_to_update.pointer_offset]), byte_size))
                                curr_val = (curr_val | (1 << addr_to_update.bit_position))

                            else:
                                curr_val = int.from_bytes(dolphin.read_bytes(addr_to_update.ram_addr, byte_size))
                                if not addr_to_update.bit_position is None:
                                    curr_val = (curr_val | (1 << addr_to_update.bit_position))
                                else:
                                    curr_val += 1

                        await self.write_bytes_and_validate(addr_to_update.ram_addr, ram_offset,
                                                       curr_val.to_bytes(byte_size, 'big'))
                    self.update_received_idx(last_recv_idx)
                    continue
                # END DYNAMIC CLIENT LOGIC
                await self.write_to_inventory(item_info, item_name, item_type)
                self.update_received_idx(last_recv_idx)

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
            return
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

                    if not self.auth:
                        self.auth = read_string(SLOT_NAME_ADDR, SLOT_NAME_STR_LENGTH)

                        # If no player name is found, disconnect DME and inform player
                        if not self.auth:
                            self.auth = None
                            self.dolphin_status = NO_SLOT_NAME_STATUS
                            logger.info(self.dolphin_status)
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

    async def write_to_inventory(self, item_info: MMXCMItemData, item_name: str, inv_type: str):
        """
        This will find the first empty inventory slot and write the item's ID to it.
        """

        if inv_type not in INVENTORY_INFO:
            logger.error(f"Error Unknown inventory type '{inv_type}' for item {item_name}.")
            return

        inv_data = INVENTORY_INFO[inv_type]
        base_address = inv_data["base_address"]
        slot_count = inv_data["slot_count"]
        slot_size = inv_data["slot_size"]

        for i in range(slot_count):
            slot_address = base_address + (i * slot_size)

            # Reads the current value of the slot
            current_item_id = dolphin.read_byte(slot_address+1)

            # If the IDs match, try to combine them
            if current_item_id == item_info.item_id:
                current_item_val = dolphin.read_byte(slot_address + 2)
                current_item_val += item_info.item_count
                dolphin.write_byte(slot_address + 2, current_item_val)
                print(f"Wrote item {item_name} to {inv_type} inventory.")
                return  # Exit after writing the item to the inventory slot.

            # A Value of 0 indicates an empty slot!
            elif current_item_id == 0:
                print(f"Found empty {inv_type} slot at address {hex(slot_address)}")
                # Get the in-game Item ID and convert it to bytes
                item_value: bytearray = bytearray(item_info.item_id.to_bytes(1, 'big'))
                item_value += item_info.item_count.to_bytes(1, 'big')
                dolphin.write_bytes(slot_address + 1, bytes(item_value))
                print(f"Wrote item {item_name} to {inv_type} inventory.")
                return  # Exit after writing the item to the inventory slot.
        logger.error(f"Error: No empty {inv_type} slots found for item {item_name}!")