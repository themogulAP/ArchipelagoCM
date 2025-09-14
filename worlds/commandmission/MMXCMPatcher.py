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

    try:
        shutil.copyfile(base_path, destination_path)
        print(f"Created a copy of the base ROM at: {destination_path}")
    except FileNotFoundError:
        print(f"Error: Base ROM not found at '{base_path}'.")
        return
    except Exception as e:
        print(f"An error occured while creating the ROM copy: {e}")
        return


