import asyncio
import json
import time
import traceback

import settings

import Patch
import Utils
from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, gui_enabled, logger, server_loop
import dolphin_memory_engine as dolphin

from NetUtils import NetworkItem, ClientStatus
from worlds.commandmission.locations import LOCATION_TABLE
from worlds.commandmission.items import ALL_ITEMS_TABLE
from MMXCMContext import MMXCMContext

# The functionality to add items, weapons, sub weapons, force metals, to our dynamic inventory. 
# RAM addresses and the slot counts for each inventory type.
# The slot is 4 away from the previous one, and the data itself is a 4 Byte.
INVENTORY_INFO = {
    "Items": {
        "base_address": 0x804A32A9,
        "slot_count": 32,
        "slot_size": 4,
    },
    "Weapons": {
        "base_address": 0x804A34B9,
        "slot_count": 120,
        "slot_size": 4,
    },
    "Sub-Weapons": {
        "base_address": 0x804A3699,
        "slot_count": 64,
        "slot_size": 4,
    },
    "Force Metals": {
        "base_address": 0x804A3329,
        "slot_count": 96,
        "slot_size": 4,
    }
}

class MMXCMCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: MMXCMContext):
        super().__init__(ctx)

    def MMXCM_cmd(self, *args):
        """
        These are the commands for our MMXCM Client.
        Serving as a place holder until we need custom commands!
        """
        print("Mega Man X: Command Mission Client.")

async def write_to_inventory(ctx: MMXCMContext, item: NetworkItem, inv_type: str):
    """
    This will find the first empty inventory slot and write the item's ID to it. 
    """
    if inv_type not in INVENTORY_INFO:
        print(f"Error Unknown inventory type '{inv_type}' for item {item.item}.")
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

        # Get the Item ID and convert it to bytes.
            item_id_bytes = struct.pack(">I", item.item)
            
        # Write the item to the empty slot.
            dolphin.write_bytes(slot_address, item_id_bytes)
            print (f"Wrote item {ctx.item_id_to_name[item.item]} ({item.item}) to {inv_type} inventory.")

        # Remove the item from the queue after it has been received.
            ctx.items_received.remove(item)
            return
    print(f"Error: No empty {inv_type} slots found for item {item.item}!")
