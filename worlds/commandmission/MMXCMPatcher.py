import os
import json
import copy
import re
from math import ceil
from random import choice, randint
import shutil 

from .Items import ALL_ITEMS_TABLE, MMXCMItemData
from .Locations import LOCATION_TABLE, MMXCMLocationData

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

    # Step 2: Apply randomization data from server.
    # The Locations key in output_data maps location IDs to Item IDs.
    with open(destination_path, "r+b") as rom_file:
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
    
                


