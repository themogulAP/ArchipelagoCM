from typing import ClassVar

from dataclasses import fields

from BaseClasses import Region, Location, Item
from worlds.AutoWorld import World
from .items import ALL_ITEMS_TABLE, FILLER_TABLE
from .locations import LOCATION_TABLE
from .rules import set_rules, REBELLION_MEDALS_GROUP
from .options import MMXCMOptions
from .files.mmxcm_rom import MMXCMPlayerContainer
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess, icon_paths

import random
import os

def run_client(*args):
    from .MMXCMClient import sync_main  # lazy import
    launch_subprocess(sync_main, name="MMMXCMClient", args=args)

# Adds the launcher for our component and our client logo.
components.append(
    Component("MMXCM Client", func=run_client, component_type=Type.CLIENT,
        file_identifier=SuffixIdentifier(".apmmxcm")))

#Define the MMX Command Mission Class:
class MMXCMWorld(World):
  """
  Mega Man X: Command Mission is a turn-based RPG set in the Mega Man X universe.
  """

# Describe the name of the game that will appear on AP Client. 
# Link options from the options py to here, and then set player options.
# Topology is for randomize maps, not needed for current implementation of static maps. 
# Data Version is the current version. 
  game: ClassVar[str] = "Mega Man X Command Mission"
  options_dataclass = MMXCMOptions
  options: MMXCMOptions
  topology_present: ClassVar[bool] = False
  data_version: ClassVar[int] = 1

  # This will tell AP what our group actually is for Rebellion Medals.
  item_name_groups: ClassVar[dict[str, frozenset[str]]] = {
        REBELLION_MEDALS_GROUP.name: REBELLION_MEDALS_GROUP.item_names
    }

#Create the dictionaries that will map every item and every location for our AP! 
  item_name_to_id: ClassVar[dict[str, int]] = {name: data.code for name, data in ALL_ITEMS_TABLE.items()}
  location_name_to_id: ClassVar[dict[str, int]] = {name: data.code for name, data in LOCATION_TABLE.items()}

#This is the very first piece of code that runs when a new MMX CM World will be created! 
  #It will then map all of our items and  to their respective Strings to IDs that we put in items and  py. 
  def __init__(self, *args, **kwargs):
    super(MMXCMWorld, self).__init__(*args, **kwargs)

# This places any logic we need to before the generation process.
  def generate_early(self): 
   pass

# This will build the entire map for our randomized AP! 
  def create_regions(self):
    # This will serve as a Master Dictionary for our loops, describing the codes needed for the same area.
    region_data = {
      "Lagrano Ruins": "Lagrano Ruins Access Code",
      "Tianna Camp": "Tianna Camp Access Code",
      "Gaudile Laboratory": "Gaudile Laboratory Access Code",
      "Ulfat Factory": "Ulfat Factory Access Code",
      "Gimialla Mine": "Gimialla Mine Access Code",
      "Vanallia Desert": "Vanallia Desert Access Code",
      "Melda Ore Plant": "Melda Ore Plant Access Code",
      "Grave Ruins Base": "Grave Ruins Base Access Code",
      "Far East HQ": "Far East HQ Access Code"
    }

    menu_region = Region("Menu", self.player, self.multiworld)
    self.multiworld.regions.append(menu_region)

    #Create our Central Tower main hub and full verision (when code is received)! 
    central_tower_hub_region = Region("Central Tower Hub", self.player, self.multiworld)
    central_tower_full_region = Region("Central Tower Full", self.player, self.multiworld)
    self.multiworld.regions.append(central_tower_hub_region)
    self.multiworld.regions.append(central_tower_full_region)

    menu_region.connect(central_tower_hub_region)

    #Connect the Regions here.
    central_tower_hub_region.connect(
      central_tower_full_region,
      rule=lambda state: state.has("Central Tower Access Code", self.player)
    )

    # Create all the other regions and connect them to the Central Tower hub!
    for region_name, access_code in region_data.items():
      new_region = Region(region_name, self.player, self.multiworld)
      self.multiworld.regions.append(new_region)

      central_tower_hub_region.connect(
        new_region,
        rule=lambda state, code=access_code: state.has(code, self.player)
      )

    # Add Every location from our  py to their regions! 
    for location_name, location_data in LOCATION_TABLE.items():
      region=self.multiworld.get_region(location_data.parent_region, self.player)
      location = Location(
        self.player,
        location_name,
        location_data.code,
        region,
      )
      region.locations.append(location)

# This will build the entire item pool for our randomized AP! 
  def create_items(self):
      item_pool = []
      for item_name, item_data in ALL_ITEMS_TABLE.items():

          # Exclude the Event item Great Redips and statically place it on the location. 
          if item_name == "Defeated Great Redips":
                continue 
        
          if "Rebellion Medal" in item_name:
                continue
          item_pool.append(self.create_item(item_name))

      self.multiworld.itempool.extend(item_pool)

    # This adds our filler items, and will calculate the number to add. 
      locations_count = len(self.multiworld.get_unfilled_locations(self.player))
      items_in_pool = len(self.multiworld.itempool)
      filler_needed = locations_count - items_in_pool

#Randomly selects the filler items to add into the pool.
      filler_items_to_add = random.choices(list(FILLER_TABLE.keys()), k=filler_needed)

      for filler_item_name in filler_items_to_add:
          self.multiworld.itempool.append(self.create_item(filler_item_name))

      # It is the helper that the create_items method calls.
  def create_item(self, name: str) -> Item:
    item_data = ALL_ITEMS_TABLE[name]
    return Item(name, item_data.classification, item_data.code, self.player)

# This will apply all the logic that we described in rules py! 
  def set_rules(self):
      set_rules(self)

  #This is where we set out rules!
  def set_completion_rules(self):
      self.multiworld.completion_condition[self.player] = lambda state: \
        state.has("Defeated Great Redips", self.player)

  # Creates the dictionary for all locations in output data, sets the path and gives us a patch to downlaod! 
  def generate_output(self, output_directory: str, **kwargs):
      # Outputs the plando details to our expected output file
      # Create the output path based on the current player + expected patch file ending.
      patch_path = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}"
                                                  f"{MMXCMPlayerContainer.patch_file_ending}")
      # Create a zip (container) that will contain all the necessary output files for us to use during patching.
      mmxcm_container = MMXCMPlayerContainer({}, patch_path, self.multiworld.player_name[self.player], self.player)
      # Write the expected output zip container to the Generated Seed folder.
      mmxcm_container.write()

def fill_slot_data(self):
    """This will provide the slot data information upon connecting to AP."""
    return {
        "rebellion_medal_count": self.options.rebellion_medal_count.value,
        "total_locations": len(LOCATION_TABLE),
        "encounter_rate": self.options.encounter_rate.value
    }
