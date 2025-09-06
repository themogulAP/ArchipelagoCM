from typing import NamedTuple, Dict, Optional, Callable
from .Items import MMXCMItemData
from .Helpers import MMXCMRamData

# This will list the exact bluepring for makign our locations! 
class MMXCMLocationData(NamedTuple):
  name:str
  code:Optional[int]
  parent_region: str
  ram_addr: Optional[MMXCMRamData] = None
  access_rule: Callable[[int], bool] = lambda state: True

# This begins the list for every single randomized item in AP.
LAGRANO_RUINS_LOCATIONS: dict[str, MMXCMLocationData] = {
  # Here is an example of the location and the bit position to track it.
  "Area 1F East MD 1": MMXCMLocationData(
    name="Area 1F East 1",
    code=1,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x804A2153, bit_position=2)
  ),
  "Area 1F East MD 2": MMXCMLocationData(
    name="Area 1F East 2", 
    code=2,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x804A2153, bit_position=3)
  ),
  "Area 2F East MD 1": MMXCMLocationData(
    name="Area 2F East 1",
    code=3,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x804A2153, bit_position=5)
  ),
  "Area 2F East MD 2": MMXCMLocationData(
    name="Area 2F East 2",
    code=4,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x804A2153, bit_position=6)
  ),
  "Area 2F East MD 3": MMXCMLocationData(
    name="Area 2F East 3",
    code=5,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x804A2153, bit_position=7)
  ),
  "Area 2F East MD 4": MMXCMLocationData(
    name="Area 2F East 4",
    code=6,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=0)
  ),
  "Area 3F East MD 1": MMXCMLocationData(
    name="Area 3F East 1",
    code=7,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=3)
  ),
  "Area 3F East MD 2": MMXCMLocationData(
    name="Area 3F East 2",
    code=8,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=2)
  ),
  "East Area Stairs 3F to 4F MD 1": MMXCMLocationData(
    name="East Area Stairs 3F to 4F 1",
    code=9,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=4)
  ),
  "Area 4F East MD 1": MMXCMLocationData(
    name="Area 4F East 1",
    code=10,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=3)
  ),
  "Area 4F East MD 2": MMXCMLocationData(
    name="Area 4F East 2",
    code=11,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=2)
  ),
  "Area 4F East MD 3": MMXCMLocationData(
    name="Area 4F East 3",
    code=12,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=1)
  ),
  "4F: Test Hall 1 MD 1": MMXCMLocationData(
  # These two entries are the MD's after Hippo is defeated.
    name="4F Test Hall 1-1",
    code=13,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=0),
    access_rule=lambda state: state.has("Hippopressor Defeated", 1) 
  ),
  "4F: Test Hall 1 MD 2": MMXCMLocationData(
    name="4F Test Hall 1-2",
    code=14,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=7),
    access_rule=lambda state: state.has("Hippopressor Defeated", 1) 
  ),
  "Area 4F West MD 1": MMXCMLocationData(
    name="Area 4F West 1",
    code=15,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=6)
  ),
  "Area 4F West MD 2": MMXCMLocationData(
    name="Area 4F West 2",
    code=16,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=5)
  ), 
  "East Area Stairs 4F to 5F MD 1": MMXCMLocationData(
    name="East Area Stairs 4F to 5F 1",
    code=17,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=5),
    access_rule=lambda state: state.has("Lagrano Key", 1) 
  ),
  "East Area Stairs 4F to 5F MD 2": MMXCMLocationData(
    name="East Area Stairs 4F to 5F 2",
    code=18,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=6),
    access_rule=lambda state: state.has("Lagrano Key", 1) 
  ),      
  "East Area Stairs 4F to 5F MD 3": MMXCMLocationData(
    name="East Area Stairs 4F to 5F 3",
    code=19,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=7),
    access_rule=lambda state: state.has("Lagrano Key", 1) 
  ),
  "Area 5F West MD 1": MMXCMLocationData(
    name="Area 5F West 1",
    code=20,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042150, bit_position=0)
  ),
  "Area 5F West MD 2": MMXCMLocationData(
    name="Area 5F West 2",
    code=21,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042150, bit_position=1)
  ), 
}
# Apply the blanket access rule to all locations that don't have an explicit rule.
for key, data in LAGRANO_RUINS_LOCATIONS.items():
    if data.access_rule is (lambda state: True):
        LAGRANO_RUINS_LOCATIONS[key] = data._replace(
            access_rule=lambda state: state.has("Lagrano Ruins Access Code", 1)
        )
          
# Location tables for other regions as they are filled. 
CENTRAL_TOWER_LOCATIONS: dict[str, MMXCMLocationData] = {}
TIANNA_CAMP_LOCATIONS: dict[str, MMXCMLocationData] = {}
GAUDILE_LABORATORY_LOCATIONS: dict[str, MMXCMLocationData] = {}
ULFAT_FACTORY_LOCATIONS: dict[str, MMXCMLocationData] = {}
GIMIALLA_MINE_LOCATIONS: dict[str, MMXCMLocationData] = {}
VANALLIA_DESERT_LOCATIONS: dict[str, MMXCMLocationData] = {}
MELDA_ORE_PLANT_LOCATIONS: dict[str, MMXCMLocationData] = {}
GRAVE_RUINS_BASE_LOCATIONS: dict[str, MMXCMLocationData] = {}
FAR_EAST_HQ_LOCATIONS: dict[str, MMXCMLocationData] = {}
MECHANILOIDS_LOCATIONS: dict[str, MMXCMLocationData] = {}
BOSS_DROPS_LOCATIONS: dict[str, MMXCMLocationData] = {}
SKY_ROOM_LOCATIONS: dict[str, MMXCMLocationData] = {}

#Dictionary for all locations.
LOCATION_TABLE: dict[str, MMXCMLocationData] = {
  **LAGRANO_RUINS_LOCATIONS,
  **CENTRAL_TOWER_LOCATIONS,
  **TIANNA_CAMP_LOCATIONS,
  **GAUDILE_LABORATORY_LOCATIONS,
  **ULFAT_FACTORY_LOCATIONS,
  **GIMIALLA_MINE_LOCATIONS,
  **VANALLIA_DESERT_LOCATIONS,
  **MELDA_ORE_PLANT_LOCATIONS,
  **GRAVE_RUINS_BASE_LOCATIONS,
  **FAR_EAST_HQ_LOCATIONS,
  **MECHANILOIDS_LOCATIONS,
  **BOSS_DROPS_LOCATIONS,
  **SKY_ROOM_LOCATIONS,
}

# A Dictionary for looking up a location by its name!
LOCATION_LOOKUP_TABLE: dict[str, MMXCMLocationData] = {
  location.name: location for location in LOCATION_TABLE.values()
}
    
