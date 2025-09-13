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

class MMXCMCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: MMXCMContext):
        super().__init__(ctx)

    def MMXCM_cmd(self, *args):
        """
        These are the commands for our MMXCM Client.
        Serving as a place holder until we need custom commands!
        """
        print("Mega Man X: Command Mission Client.")

# The functionality to add items, weapons, sub weapons, force metals, to our dynamic inventory. 
INVENTORY_INFO = {
    "Items": {
        "base_address": 0x804A32A9,
        "slot_count": 32,
        "slot_size": 4,
    }.
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

    
