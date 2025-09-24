import os 
import json 
import copy 
import re 
from math import ceil 
from random import choice, randint 
import shutil 
import struct

from gclib.gcm import GCM 
from gclib.dol import DOL 

from .Items import ALL_ITEMS_TABLE, MMXCMItemData 
from .Locations import LOCATION_TABLE, MMXCMLocationData 

# This is our section that will iilustrate the direct code changes we need to make... before any randomization. 
# If adding more changes: fill in this dictionary with the address and new bytes.  
CODE_PATCHES = [ 
    { 
        # Prevent Party Members From Leaving ------------- Party Member Slot Strings 
        # Original RAM Address: 800d7E0C 
        "address": 0x0D4E0C, 
        "data": [0x60, 0x00, 0x00, 0x00]  # NOP Instruction 
    }, 
    { 
        # Prevent Party Members From Leaving ----------- # Of Party Members 
        # Original Ram: 800d7e2c 
        "address": 0x0D4E2C, 
        "data": [0x38, 0x06, 0x00, 0x00]  # Sets the character substraction to 0.  
    }, 
    { 
        # Loading into Arcade: Scenario Flag 
        # RAM Address: 800Dbab4 
        "address": 0x0AAB4, 
        "data": [0x38, 0x60, 0x00, 0x0A] 
    }, 
    { 
        # Loading into Arcade: Stage # 
        # RAM: 80011d04 
        "address": 0x0ED04, 
        "data": [0x3C, 0x60, 0x00, 0x02] 
    }, 
    { 
        # Loading into arcade: Area # and Spawn Letter 
        # RAM: 80011d08 
        "address": 0x0ED08, 
        "data": [0x38, 0x03, 0x05, 0x4C] 
    }, 
    { 
        # Set Flag Arakure, and Chpt 10 Cutscene, and Boss3 
        # RAM: 8000d8f8 
        "address": 0x0A8F8, 
        "data": [0x38, 0x60, 0x00, 0x03] 
    }, 
    { 
        # Store flag Arakure, Chpt 10 Cutscene, and Boss3 
        # RAM: 8000d8fc 
        "address": 0x0A8FC, 
        "data": [0x90, 0x64, 0x00, 0x45] 
    }, 
    { 
        # Sets register back to zero 
        # RAM: 8000D900 
        "address": 0x0A900, 
        "data": [0x38, 0x60, 0x00, 0x00] 
    }, 
    { 
        # Sets cutscenes Intruders and Spider Fight 
        # RAM: 8000d908 
        "address": 0x0A908, 
        "data": [0x38, 0x60, 0x00, 0xC0] 
    }, 
    { 
        # Stores cutscene for Intruders + Spider Fight 
        # RAM: 8000d90c 
        "address": 0x0A90C, 
        "data": [0x90, 0x64, 0x00, 0x5A] 
    }, 
    { 
        # Sets the Arcade Door to Open 
        # RAM: 8000d910 
        "address": 0x0A910, 
        "data": [0x38, 0x60, 0x00, 0x01] 
    }, 
    { 
        # Stores the Arcade Door Open flag 
        # RAM: 8000d914 
        "address": 0x0A914, 
        "data": [0x90, 0x64, 0x00, 0x06] 
    }, 
    { 
        # sets every other flag back to zero 
        # RAM: 8000d918 
        "address": 0x0A918, 
        "data": [0x38, 0x60, 0x00, 0x00] 
    }, 
    { 
        # Stores every other flag to zero 
        # RAM: 8000d91c 
        "address": 0x0A91C, 
        "data": [0x90, 0x64, 0x00, 0x64] 
    }, 
    { 
        # Prevent beating the Game --- Change comparison 
        # RAM Address: 8001047c 
        "address": 0x0D47C, 
        "data": [0x2c, 0x04, 0x00, 0x3D] 
    }, 
    { 
        # Change the equation to add zero to scenario flag 
        # RAM: 800104c4 
        "address": 0x0D4C4, 
        "data": [0x38, 0x03, 0x00, 0x00] 
    }, 
    { 
        # Set Every Previous Chapter Flag to Unclear 
        # RAM: 800104e8 
        "address": 0x0D4E8, 
        "data": [0x60, 0x00, 0x00, 0x00] 
    }, 
    { 
        # Change Lagrano Ruins to teleport back to Central Tower STAGE w/o Access Code 
        # RAM Address Label: 80082fac 
        "address": 0x07ffa4, 
        "data": [0x3c, 0x80, 0x00, 0x02] 
    }, 
    { 
        # Change Lagrano Ruins AREA back to Shopping Arcade w/o Access Code 
        # RAM: 80082fac 
        "address": 0x07ffac, 
        "data": [0x38, 0x04, 0x05, 0x4F] 
    }, 
    { 
        # Change Tianna Camp Stage to Central Tower w/o Access Code 
        # RAM Address: 80082fcc 
        "address": 0x07ffcc, 
        "data": [0x3c, 0x80, 0x00, 0x02] 
    }, 
    { 
        # Change Tianna Camp AREA to Central Tower... 
        # RAM: 80082fd4 
        "address": 0x07ffd4, 
        "data": [0x38, 0x04, 0x05, 0x4F] 
    }, 
    { 
        # Changes Gaudile Laboratory back to Central Tower 
        # RAM: 80082ff4 
        "address": 0x07fff4, 
        "data": [0x3c, 0x80, 0x00, 0x02] 
    }, 
    { 
        # Changes Gaudile Laboratory back to Shopping Arcade 
        # RAM: 80082ffc 
        "address": 0x07fffc, 
        "data": [0x38, 0x04, 0x05, 0x4F] 
    }, 
    { 
        # Changes Ulfat Factory to Central Tower teleport 
        # RAM Address: 8008301c 
        "address": 0x08001c, 
        "data": [0x3c, 0x80, 0x00, 0x02] 
    }, 
    { 
        # Changes Ulfat Factory AREA to Shopping Arcade 
        # RAM: 80083204 
        "address": 0x080024, 
        "data": [0x38, 0x04, 0x05, 0x4F] 
    }, 
    { 
        # Changes Gimialla Mine to Central Tower stage 
        # RAM Address: 80083044 
        "address": 0x080044, 
        "data": [0x3c, 0x80, 0x00, 0x02] 
    }, 
    { 
        # Changes Gimialla Mine AREA to Shopping Arcade 
        # RAM: 8008304c 
        "address": 0x08004c, 
        "data": [0x38, 0x04, 0x05, 0x4F] 
    }, 
    { 
        # Changes Melda Ore Plant to Central Tower Stage 
        # RAM: 80083094 
        "address": 0x080094, 
        "data": [0x3c, 0x80, 0x00, 0x02] 
    }, 
    { 
        # Changes Melda Ore Plant AREA to Shopping Arcade 
        # RAM: 8008309c 
        "address": 0x08009c, 
        "data": [0x38, 0x04, 0x05, 0x4F] 
    }, 
    { 
        # Changes Grave Ruins Base to Central Tower Stage 
        # RAM: 800830bc 
        "address": 0x0800BC, 
        "data": [0x3c, 0x80, 0x00, 0x02] 
    }, 
    { 
        # Changes Grave Ruins Base AREA to Shopping Arcade 
        # RAM: 800830c4 
        "address": 0x0800c4, 
        "data": [0x38, 0x04, 0x05, 0x4F] 
    } 
] 


class MMXCMPatcher:
    def __init__(self, clean_iso_path, randomized_output_file_path):
        self.clean_iso_path = clean_iso_path
        self.randomized_output_file_path = randomized_output_file_path
        self.gcm = None
        self.dol = None

    def write_item_to_location(self, location_name: str, item_name: str):
        """
        This function to look up the correct addresses and IDs and write the new item into the ROM.
        """
        try:
            # 1 - We will look up the locations address from Location table
            if location_name not in LOCATION_TABLE:
                print(f"Warning: Skipping unknown '{location_name}'.")
                return
            location_data: MMXCMLocationData = LOCATION_TABLE[location_name]
            dol_address = location_data.dol_address

            # 2 - Look up the Item's ID from ALL_ITEMS_TABLE
            if item_name not in ALL_ITEMS_TABLE:
                print(f"Warning: Skipping Unknown Item '{item_name}'.")
                return
            item_data: MMXCMItemData = ALL_ITEMS_TABLE[item_name]
            # This access our item ID from our Data class to tell this randomizer WHICH item it is. 
            # I.e. X Buster = 25
            item_rom_id = item_data.item_id

            # Writes the New Item ID to the DOL - - - - -
            # This coverts the Item ID into the byte sequence.
            item_id_bytes = struct.pack(">I", item_rom_id)
            self.dol.data.seek(dol_address)
            self.dol.data.write(item_id_bytes)

        except Exception as e:
            print(f"An error occured while writing data for location '{location_name}' and item '{item_name}': {e}")
            return
    ### NEW CODE END ###


    def create_patch(self, output_data: dict, base_path: str, destination_path: str): 
        """ 
        This function will take the base ROM, apply our changes and randomization data, and save the patched ROM. 
        """ 
        self.gcm = GCM(self.clean_iso_path)  # We will path this to the Vanilla ROM!  
        self.gcm.read_entire_disc() 
        self.dol = DOL() 

        self.dol = self.gcm.read_dol_from_disc() 

        print("Applying Internal Code Patches...") 

        for patch in CODE_PATCHES: 
            try: 
                address = patch["address"] 
                data_to_write = bytes(patch["data"]) 
            
                # Seeks the specific DOL Offset. 
                self.dol.data.seek(address) 
            
                # Write the new bytes, overwriting old PowerPc command. 
                self.dol.data.write(data_to_write) 
            
                # We want to have GClib just do this to target the DOL!  
            
                print(f"Wrote {len(data_to_write)} bytes at address {hex(address)}.") 
            except KeyError as e: 
                print(f"Skipping malformed patch data: missing key {e}") 
            except Exception as e: 
                print(f"An error occured while applying a code patch: {e}") 
        print("Internal code patching complete.")

        #This is the loop for calling the REFACTORED item to location information above. 
        print("Applying Randomized Item Patches...")
        for location_name, item_name in output_data["locations"].items():
            self.write_item_to_location(location_name, item_name)
        print("Randomized item patching complete!")
        
        # Save all changes to the DOL itself. 
        self.dol.save_changes() 
        self.gcm.changed_files["sys/main.dol"] = self.dol.data 
        
        # Generator function to combine all necessary files into an ISO file. 
        # Returned information is ignored. 
        for _, _ in self.export_files_from_memory(): 
            continue 


    # If Export to disc is true, Exports the entire file/directory contents of the ISO to specified folder 
    # Otherwise, creates a direct ISO file. 
    def export_files_from_memory(self): 
        yield from self.gcm.export_disc_to_iso_with_changed_files(self.randomized_output_file_path)
