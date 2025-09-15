import os
import json
import copy
import re
from math import ceil
from random import choice, randint
import shutil 

from .Items import ALL_ITEMS_TABLE, MMXCMItemData
from .Locations import LOCATION_TABLE, MMXCMLocationData

#This is our section that will iilustrate the direct code changes we need to make... before any randomization.
# If adding more changes: fill in this dictionary with the address and new bytes. 
CODE_PATCHES = [
     {
         # Prevent Party Members From Leaving ------------- Party Member Slot Strings
         #Original RAM Address: 800d7E0C
         "address": 0x0D4E0C,
         "data": [0x60, 0x00, 0x00, 0x00] #NOP Instruction
     },
     {
         # Prevent Party Members From Leaving ----------- # Of Party Members
         # Original Ram: 800d7e2c
         "address": 0x0D4E2C,
         "data": [0x38, 0x06, 0x00, 0x00] # Sets the character substraction to 0. 
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
     }
     {
        # Set Every Previous Chapter Flag to Unclear
        # RAM: 800104e8
        "address": 0x0D4E8,
        "data": [0x60, 0x00, 0x00, 0x00]
    },
]
    

def __get_item_name(item_data, slot: int):
    """
    This will give us the correct in game name for each item based on item_data
    """
    # - Put the item name conversion logic here
    pass

def create_patch(output_data: dict, base_path: str, destination_path: str):
    """
    This function will take the base ROM, apply our changes and randomization data, and save the patched ROM.
    """

    # Step 1: Find and copy the Base Rom, as to not be destructive.
    try:
        shutil.copyfile(base_path, destination_path)
        print(f"Created a copy of the base ROM at: {destination_path}")
    except FileNotFoundError:
        print(f"Error: Base ROM not found at '{base_path}'.")
        return
    except Exception as e:
        print(f"An error occured while creating the ROM copy: {e}")
        return

    # Step 2: Apply our internal code patches as described earlier. 
    with open(destination_path, "r+b") as rom_file: 
        print("Applying Internal Code Patches...")
        for patch in CODE_PATCHES:
            try:
                 address = patch["address"]
                 data_to_write = bytes(patch["data"])

               #Seeks the specific DOL Offset.
                 rom_file.seek(address)

               # Write the new bytes, overwriting old PowerPc command.
                 rom_file.write(data_to_write)

                 print(f"Wrote {len(data_to_write)} bytes at address {hex(address)}.")
            except KeyError as e:
                 print(f"Skipping malformed patch data: missing key {e}")
            except Exception as e:
                 print(f"An error occured while applying a code patch: {e}")
        print("Internal code patching complete.")         
         
    # Step 3: Apply randomization data from server.
    # The Locations key in output_data maps location IDs to Item IDs.
        randomized_locations = output_data.get("locations", {})
        for location_id, item_id in randomized_locations.items():
            try:
                # Find the location data based on AP ID.
                location_name = next(name for name, data in LOCATION_TABLE.items() if data.ap_id == location_id)
                location_data = LOCATION_TABLE[location_name]

                #Find the item based on its AP ID. 
                item_data = next(data for name, data in ALL_ITEMS_TABLE.items() if data.ap_id == item_id)

                # Get the RAM Address and Bit position we will write to. 
                ram_address = location_data.ram_addr.address
                bit_position = location_data.ram_addr.bit_position

                rom_file.seek(ram_address)

                #Read the Current byte.
                current_byte = rom_file.read(1)[0]

                #Determine the new byte value.
                new_byte = current_byte | (1 << bit_position)

                #Seek the address before writing
                rom_file.seek(ram_address)

                #Write the new byte value.
                rom_file.write(bytes([new_byte]))

                print(f"Patched '{location_name}' with item '{item_data.name}'.")
            except (StopIteration, KeyError) as e:
                print(f"Error finding location or item data for IDs: {location_id}, {item_id}. Error: {e}")
            except Exception as e:
                print(f"An unexpected error occured during patching: {e}")

    print("Patching Complete.")
    
            


