import asyncio
import struct
import sys
import traceback
from typing import Dict

import NetUtils
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, logger, server_loop
import dolphin_memory_engine as dolphin

from NetUtils import NetworkItem
from worlds.commandmission.helpers import CONNECTION_INITIAL_STATUS, CONNECTION_CONNECTED_STATUS, \
    CONNECTION_REFUSED_STATUS, CONNECTION_VERIFY_SERVER, CONNECTION_LOST_STATUS
from worlds.commandmission.locations import LOCATION_TABLE
from worlds.commandmission.items import ALL_ITEMS_TABLE
from worlds.tww.TWWClient import read_string


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

async def wait_for_next_loop(time_to_wait: int):
    await asyncio.sleep(time_to_wait)


# Starts the full loop and debug messages for connecting to Dolphin.
async def dolphin_connect_loop(ctx: CommonContext):
    """
    Connects to the Dolphin emulator and waits for the correct game to be running.
    """
    while not ctx.exit_event.is_set():
        try:
            if not dolphin.is_hooked():
                dolphin.hook()
                if dolphin.get_status() == dolphin.get_status().no_emu or dolphin.get_status() == dolphin.get_status().notRunning:
                    dolphin.un_hook()
                ctx.dolphin_status = CONNECTION_INITIAL_STATUS
                logger.info(ctx.dolphin_status)
                await wait_for_next_loop(5)
                continue

            # If the Game ID is a standard one, disconnect because it isnt the randomized ROM.
            if not ctx.dolphin_status == CONNECTION_CONNECTED_STATUS:
                game_id = read_string(0x80000000, 6)
                if game_id in ["GXRP08"]:
                    logger.info(CONNECTION_REFUSED_STATUS)
                    ctx.dolphin_status = CONNECTION_REFUSED_STATUS
                    dolphin.un_hook()
                    await wait_for_next_loop(5)
                    continue

            ctx.locations_checked = set()

            # Inform player we are ready for connection
            if not ctx.dolphin_status == CONNECTION_VERIFY_SERVER:
                ctx.dolphin_status = CONNECTION_VERIFY_SERVER
                logger.info(ctx.dolphin_status)
            await ctx.server_auth()

            if not ctx.slot:
                await wait_for_next_loop(5)
                continue

        except Exception:
            dolphin.un_hook()
            logger.error(traceback.format_exc())
            logger.info("Connection to Dolphin failed, attempting in 5 seconds...")
            ctx.dolphin_status = CONNECTION_LOST_STATUS
            await ctx.disconnect()
            await asyncio.sleep(5)
            continue


class MMXCMCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: 'MMXCMContext'):
        super().__init__(ctx)

    def _cmd_mmxcm(self, *args):
        """
        These are the commands for our MMXCM Client.
        Serving as a place holder until we need custom commands!
        """
        print("Mega Man X: Command Mission Client.")

class MMXCMContext(CommonContext):
    command_processor = MMXCMCommandProcessor
    game = "Mega Man X: Command Mission"
    items_handling = 0b111
    dolphin_connected: bool = False
    seed_verified: bool = False
    slot_data: dict | None = {}
    checked_locations = set()

    item_id_to_name: Dict[int, str]

    slot_to_player_name: Dict[int, str]

    def __init__(self, server_address, password):
        """
        Initialize the MMXCM Context
        :param server_address: Address of AP Server.
        :param password: Password for the server.
        """
        super().__init__(server_address, password)

        #List the variables needed for connection.
        self.slot = None
        self.slot_data = None
        self.team =None

        self.items_received = []

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(MMXCMContext, self).server_auth(password_requested)

        await self.get_username() # Gets the player name and alias.
        await self.send_connect() # Sends final Connection packet to server.

    def on_package(self, cmd: str, args: dict):
        """
        Handles the incoming network pakages from the server.
        """
        super().on_package(cmd,args)

        slot_data = args.get("slot_data", {})

        match cmd:
            case "Connected":

                # Seed verification step.
                arg_seed = str(slot_data["seed"])

                try:
                    #Read the ISO seed #
                    iso_seed = read_string(0x80000001, len(arg_seed))
                except Exception:
                    iso_seed = ""

                if arg_seed != iso_seed:
                    print("Error! Incorrect Randomized MMXCM Iso File. Seed does not match!")
                else:
                    self.seed_verified = True
                    print("Game seed verified successfully")

                self.slot_data = slot_data
                print("Successfully connected to the Archipelago server!")

            case "ReceivedItems":
                # This is the package sent when we get something from a different player.
                items_to_add = []
                for item in args["items"]:
                    # This is the format of the item.
                    items_to_add.append(NetworkItem(*item))

                self.items_received.extend(items_to_add)

    async def disconnect(self, allow_autoreconnect: bool = False):
        await super().disconnect(allow_autoreconnect)

        self.slot = None
        self.team = None
        self.slot_data = None
        self.checked_locations = set()
        self.seed_verified = False
        self.dolphin_connected = False

async def write_to_inventory(ctx: MMXCMContext, item: NetworkItem, inv_type: str):
    """
    This will find the first empty inventory slot and write the item's ID to it.
    """
    # Look up the item's data using its name, not its Archipelago ID
    item_info = ALL_ITEMS_TABLE.get(ctx.item_id_to_name[item.item])

    if not item_info:
        print(f"Error: Could not find item information for item ID {item.item}.")
        return

    if inv_type not in INVENTORY_INFO:
        print(f"Error Unknown inventory type '{inv_type}' for item {ctx.item_id_to_name[item.item]}.")
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
            print(f"Wrote item {ctx.item_id_to_name[item.item]} ({item.item}) to {inv_type} inventory.")
            return  # Exit after writing the item to the inventory slot.
    print(f"Error: No empty {inv_type} slots found for item {item.item}!")


async def mmxcm_update_non_savable_ram(self):
    value_to_write = bytes([1])
    memory_address = -0x804A20B1

    try:
        while True:
            dolphin.write_bytes(memory_address, value_to_write)
            # Add the small delay to prevent the loop.
            await asyncio.sleep(0.1)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("RAM write operation has stopped.")


async def game_watcher(ctx: MMXCMContext):
    """
    This is the main loop that will handle checking locations and giving items.
    It will run as long as the client is connected to the server.
    """

    # This initializes the set locations checked.
    checked_locations_in_game = set()

    # This will track the medals we have reported.
    reported_medals = set()

    while not ctx.finished_game:
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
                    print(f"Error reading location '{location_name}' at address {hex(ram_data.ram_addr)}: {e}")

        if newly_checked_locations:
            print(f"Found new locations: {newly_checked_locations}")
            await ctx.check_locations(newly_checked_locations)

        if not ctx.finished_game:
            try:
                # Get the RAM data for the Great Redips event. This is our "beating the game".
                redips_ram_data = LOCATION_TABLE["Defeated Great Redips"].ram_addr

                if redips_ram_data:
                    # Read the value at the event's memory address.
                    boss_defeated_value = dolphin.read_bytes(redips_ram_data.ram_addr, 1)[0]

                    # Check if the bit for defeating Redips is set.
                    if boss_defeated_value == 9:
                        print("Final boss defeated! Signaling game completion to the server.")
                        ctx.finished_game = True  # This ends the while loop on the next pass.
                        await ctx.send_msgs([{
                            "cmd": "StatusUpdate",
                            "status": NetUtils.ClientStatus.CLIENT_GOAL,
                        }])
            except Exception as e:
                # This will catch errors if the game state is not readable or the address is invalid.
                print(f"Error checking for game completion: {e}")

        # Check for new items.
        while ctx.items_received:
            item_to_add = ctx.items_received.pop(0)

            item_name = ctx.item_id_to_name[item_to_add.item]
            player_name = ctx.slot_to_player_name[item_to_add.player]
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
                    print(f"Error while writing to RAM for Lagrano Access Code: {e}")

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
                    print(f"Error while writing to RAM for Central Tower Access Code: {e}")

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
                    print(f"Error while writing to RAM for Tianna Camp Access Code: {e}")

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
                    print(f"Error while writing to RAM for Gaudile Laboratory Access Code: {e}")

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
                    print(f"Error while writing to RAM for Ulfat Factory Access Code: {e}")

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
                    print(f"Error while writing to RAM for Gimialla Mine Access Code: {e}")

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
                    print(f"Error while writing to RAM for Vanallia Desert Access Code: {e}")

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
                    print(f"Error while writing to RAM for Melda Ore Plant Access Code: {e}")

                continue

            elif item_name == "Grave Ruins Base Access Code":
                print("Grave Ruins Base Access Code received! Patching RAM to enable the teleporter.")
                try:
                    # Write the first PowerPC instruction.
                    dolphin.write_bytes(0x800830bc, b'\x3c\x80\x00\x09')

                    # Write the second PowerPC instruction.
                    dolphin.write_bytes(0x800830c4, b'\x38\x04\x01\x41')

                except Exception as e:
                    print(f"Error while writing to RAM for Grave Ruins Base Access Code: {e}")

                continue
            # --- ---------------------------END DYNAMIC CLIENT LOGIC ------------------------------------------------------

            item_info = ALL_ITEMS_TABLE.get(item_name)

            if item_info and "type" in item_info:
                item_type = item_info["type"]
                await write_to_inventory(ctx, item_to_add, item_type)
            else:
                print(f"Error: Could not find type information for item ID {item_to_add.item}.")

        await asyncio.sleep(1)  # Can set this so sleep to avoid CPU usage.

    print("Disconnected from Dolphin.")


async def async_main(*launch_args: str):
    """
    This is the main function that will be called by the `CommonClient`
    to start our client.
    """

    try:
        parser = get_base_parser()
        parser.add_argument('apmmxcm_file', default="", type=str, nargs="?", help='Path to an APMMXCM file')
        args = parser.parse_args(launch_args)

        if args.apmmxcm_file:
            from .MMXCMPatcher import MMXCMPatcher
            mmxcm_patch = MMXCMPatcher(args.apmmxcm_file)
            mmxcm_patch.create_patch()

        # Create our context and initialize the command processor.
        ctx = MMXCMContext(args.connect, args.password)
        ctx.command_processor = MMXCMCommandProcessor

        # Run the client!
        ctx.run_gui()
        ctx.run_cli()

        await dolphin_connect_loop(ctx)

        ctx.dolphin_sync_task = asyncio.create_task(server_loop(ctx), name="MMXCM GameWatcher")

        if ctx.dolphin_sync_task:
            await ctx.dolphin_sync_task
    except Exception as genericEx:
        print("Unable to run dolphin async. Ex: " + str(genericEx))


if __name__ == "__main__":
    # This ensures that the script will run the main function when executed.
    async_main(*sys.argv[1:])