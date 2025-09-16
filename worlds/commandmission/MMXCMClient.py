import asyncio
import json
import struct
import time
import traceback
import typing

import settings

import Patch
import Utils
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, logger, server_loop
import dolphin_memory_engine as dolphin

from NetUtils import NetworkItem, ClientStatus
from worlds.commandmission.locations import LOCATION_TABLE
from worlds.commandmission.items import ALL_ITEMS_TABLE
from MMXCMContext import MMXCMContext
from . import helpers

# Starts the full loop and debug messages for connecting to Dolphin.
async def dolphin_connect_loop(ctx: CommonContext):
    """
    Connects to the Dolphin emulator and waits for the correct game to be running.
    """
    while True:
        try:
            if not dolphin.is_hooked():
                dolphin.hook()

            if dolphin.get_status() == dolphin.Dolphin.DolphinStatus.no_emu or \
               dolphin.get_status() == dolphin.Dolphin.DolphinStatus.not_running:
                if dolphin.is_hooked():
                    dolphin.un_hook()
                print("Dolphin not running. Waiting for emulator...")
                await asyncio.sleep(5)
                continue

            game_id = dolphin.read_bytes(0x80000000, 4)
            if game_id.decode("ascii") not in ["GXRP08", "GXRP01"]:
                print("Incorrect game ID. Make sure Mega Man X: Command Mission is running.")
                if dolphin.is_hooked():
                    dolphin.un_hook()
                await asyncio.sleep(5)
                continue
            
            print("Connected to Dolphin with the correct game running.")
            break

        except Exception as e:
            if dolphin.is_hooked():
                dolphin.un_hook()
            print(f"Could not connect to Dolphin: {e}")
            print("Retrying in 5 seconds...")
            await asyncio.sleep(5)
            continue

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

class MMXCMCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: MMXCMContext):
        super().__init__(ctx)

    def _cmd_mmxcm(self, *args):
        """
        These are the commands for our MMXCM Client.
        Serving as a place holder until we need custom commands!
        """
        print("Mega Man X: Command Mission Client.")

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
            print (f"Wrote item {ctx.item_id_to_name[item.item]} ({item.item}) to {inv_type} inventory.")
            return # Exit after writing the item to the inventory slot.
    print(f"Error: No empty {inv_type} slots found for item {item.item}!")

async def game_watcher(ctx: MMXCMContext):
    """
    This is the main loop that will handle checking locations and giving items.
    It will run as long as the client is connected to the server.
    """
    try:
        # Connect to the Dolphin Emulator
        dolphin.connect()
        print("Connected to Dolphin.")
    except Exception as e:
        print(f"Could not connect to Dolphin: {e}")
        ctx.gui_enabled = False
        return

    # Check for the game ID to make sure we are connected to MMX CM!
    game_id = dolphin.read_bytes(0x80000000, 4)
    if game_id.decode("ascii") not in ["GXRP08", "GXRP01"]:
        print("Incorrect game ID. Make sure Mega Man X: Command Mission is running.")
        dolphin.disconnect()
        ctx.gui_enabled=False
        return

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
                # Reads the value at the locations RAM address.
                try:
                    ram_data = location_info.get("ram_addr")
                    if ram_data:
                        # Read the value at the locations RAM address.
                        location_value = dolphin.read_bytes(ram_data.ram_addr, 1)[0]
                        # Check if the location's bit position has been set in the value.
                        if (location_value & (1 << ram_data.bit_position)) > 0:
                            newly_checked_locations.append(location_name)
                            checked_locations_in_game.add(location_name)
                except Exception as e:
                    print(f"Error reading location '{location_name}' at address {hex(location_info['ram_addr'])}: {e}")

        if newly_checked_locations:
            print(f"Found new locations: {newly_checked_locations}")
            await ctx.send_checked_locations(newly_checked_locations)

        if not ctx.finished_game:
            try:
                # Get the RAM data for the Great Redips event. This is our "beating the game". 
                redips_ram_data = LOCATION_TABLE["Defeated Great Redips"].get("ram_addr")

                if redips_ram_data:
                    # Read the value at the event's memory address.
                    boss_defeated_value = dolphin.read_bytes(redips_ram_data.ram_addr, 1)[0]

                    # Check if the bit for defeating Redips is set.
                    if (boss_defeated_value & (1 << redips_ram_data.bit_position)) > 0:
                        print("Final boss defeated! Signaling game completion to the server.")
                        await ctx.send_goal()
                        ctx.finished_game = True  # This ends the while loop on the next pass.
            except Exception as e:
                # This will catch errors if the game state is not readable or the address is invalid.
                print(f"Error checking for game completion: {e}")
        
        # Check for new items.
        while ctx.items_received:
            item_to_add = ctx.items_received.pop(0)

            item_name = ctx.item_id_to_name[item_to_add.item]
            player_name = ctx.slot_to_player_name[item_to_add.player]
            print(f"Received item: {item_name} from {player_name}.")
            
            item_info = ALL_ITEMS_TABLE.get(item_name)

            if item_info and "type" in item_info:
                item_type = item_info["type"]
                await write_to_inventory(ctx, item_to_add, item_type)
            else:
                print(f"Error: Could not find type information for item ID {item_to_add.item}.")

        await asyncio.sleep(1) # Can set this so sleep to avoid CPU usage.

    dolphin.disconnect()
    print("Disconnected from Dolphin.")

async def _async_main():
    """
    This is the main function that will be called by the `CommonClient`
    to start our client.
    """
    parser = get_base_parser(ctx_defaults={"game": "Mega Man X: Command Mission"})
    args = parser.parse_args()

    # Create our context and initialize the command processor.
    ctx = MMXCMContext(args.connect, args.password)
    ctx.command_processor = MMXCMCommandProcessor(ctx)

    # Run the client!
    ctx.run_gui = gui_enabled

    await server_loop(ctx, game_watcher, "Game")

if __name__ == "__main__":
    # This ensures that the script will run the main function when executed.
    asyncio.run(_async_main())
