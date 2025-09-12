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

  item_name_to_id: ClassVar[dict[str, int]] = {name: data.ap_id for name, data in ALL_ITEMS_TABLE.items()}
  location_name_to_id: ClassVar[dict[str, int]] = {name: data.ap_id for name, data in LOCATION_TABLE.items()}

  def __init__(self, multiworld, player):
    super().__init__(multiworld, player)
    self.location_name_to_id = LOCATION_TABLE.ap_ids
    self.item_name_to_id = ALL_ITEMS_TABLE.ap_ids

  def generate_early(self): 
    pass

  def create_regions(self):
    pass

  def create_items(self):
    pass

  def set_rules(self):
      set_rules(self)

  def fill_slot_data(self):
      return {}
    
    
