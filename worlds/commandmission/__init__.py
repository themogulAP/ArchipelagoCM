from typing import ClassVar
from worlds.AutoWorld import World
from .Items import ALL_ITEMS_TABLE
from .Locations import LOCATION_TABLE
from .Rules import set_rules
from .Options import MMXCMOptions

#Define the MMX Command Mission Class:
class MMXCMWorld(World):
  """
  Mega Man X: Command Mission is a turn-based RPG set in the Mega Man X universe. 
  """

# Describe the name of the game that will appear on AP Client. 
# Link options from the options py to here, and then set player options.
# Topology is for randomize maps, not needed for current implementation of static maps. 
# Data Version is the current version. 
  game: ClassVar[str] = "Mega Man X: Command Mission"
  option_dataclass: ClassVar[MMXCMOptions]
  options: MMXCMOptions
  topology_present: ClassVar[bool] = False
  data_version: ClassVar[int] = 1

#Create the dictionaries that will map every item and every location for our AP! 
  item_name_to_id: ClassVar[dict[str, int]] = {name: data.ap_id for name, data in ALL_ITEMS_TABLE.items()}
  location_name_to_id: ClassVar[dict[str, int]] = {name: data.ap_id for name, data in LOCATION_TABLE.items()}

#This is the very first piece of code that runs when a new MMX CM World will be created! 
  #It will then map all of our items and locations to their respective Strings to IDs that we put in items and locations py. 
  def __init__(self, multiworld, player):
    super().__init__(multiworld, player)
    self.location_name_to_id = LOCATION_TABLE.ap_ids
    self.item_name_to_id = ALL_ITEMS_TABLE.ap_ids

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
    
    # Create the virtual "starting area" for the game.
    menu_region = Region("Menu", self.player, self.multiworld)
    self.multiworld.regions.append(menu_region)

    #Create our Central Tower main hub and full verision (when code is received)! 
    central_tower_hub_region = Region("Central Tower Hub", self.player, self.multiworld)
    central_tower_full_region = Region("Central Tower Full", self.player, self.multiworld)
    self.multiworld.regions.append(central_tower_hub_region)
    self.multiworld.regions.append(central_tower_full_region)

    #Connect the Regions here.
    menu_region.connect(central_tower_hub_region)
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

    # Add Every location from our locations py to their regions! 
    for location_name, location_data in LOCATION_TABLE.items():
      region=self.multiworld.get_region(location_data.parent_region, self.player)
      location = Location(
        self.player,
        location_name,
        location_data.ap_id,
        region,
      )
      region.locations.append(location)

# This will build the entire item pool for our randomized AP! 
  def create_items(self):
      item_pool = []
      for item_name, item_data in ALL_ITEMS_TABLE.items():
          item_pool.append(self.create_item(item_name))

      self.multiworld.itempool.extend(item_pool)

# This will apply all the logic that we described in rules py! 
  def set_rules(self):
      set_rules(self)

# This will bridge the game between the server that generates the seed and the client! 
  # Example: this will tell the patcher to fix the encounter rate! 
  def fill_slot_data(self):
      slot_data = {
          "rebellion_medal_count": self.options.rebellion_medal_count.value,
          "total_locations": len(LOCATION_TABLE),
          "encounter_rate": self.options.encounter_rate.value
      }
      return slot_data
    
    
