from typing import NamedTuple, Dict, Optional, Callable
from .Items import MMXCMItemData
from .Helpers import MMXCMRamData

#This will define a constant for easy comparison. 
DEFAULT_RULE: Callable[[int], bool] = lambda state: True

# This will list the exact blueprint for making our locations! 
class MMXCMLocationData(NamedTuple):
  name:str
  code:Optional[int]
  parent_region: str
  ram_addr: Optional[MMXCMRamData] = None
  access_rule: Callable[[int], bool] = DEFAULT_RULE

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
    if data.access_rule is DEFAULT_RULE:
        LAGRANO_RUINS_LOCATIONS[key] = data._replace(
            access_rule=lambda state: state.has("Lagrano Ruins Access Code", 1)
        )
          
# Location tables for other regions as they are filled. 
CENTRAL_TOWER_LOCATIONS: dict[str, MMXCMLocationData] = {
  "Shaft 999F MD 1": MMXCMLocationData(
    name="Shaft 999F 1",
    code=22,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2150, bit_position=6)
  ),
  "Shaft 999F MD 2": MMXCMLocationData(
    name="Shaft 999F 2",
    code=23,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2150, bit_position=4)
  ),
  "Shaft 999F MD 3": MMXCMLocationData(
    name="Shaft 999F 3",
    code=24,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2150, bit_position=5)
  ),
  "Access Tunnel E-1 East MD 1": MMXCMLocationData(
    name="Access Tunnel E-1 East 1",
    code=25,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2154, bit_position=4)
  ),
  "Access Tunnel E-1 East MD 2": MMXCMLocationData(
    name="Access Tunnel E-1 East 2",
    code=26,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2154, bit_position=5)
  ),
  "Access Tunnel E-1 North MD 1": MMXCMLocationData(
    name="Access Tunnel E-1 North 1",
    code=27,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2154, bit_position=2)
  ),
  "Access Tunnel E-1 North MD 2": MMXCMLocationData(
    name="Access Tunnel E-1 North 2",
    code=28,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2154, bit_position=3)
  ),
  "Access Tunnel E-1 North MD 3": MMXCMLocationData(
    name="Access Tunnel E-1 North 3",
    code=29,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2154, bit_position=6)
  ),
  "Tower Base Access Tunnel MD 1": MMXCMLocationData(
    name="Tower Base Access Tunnel 1",
    code=30,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=6)
  ),
  "Tower Base Access Tunnel MD 2": MMXCMLocationData(
    name="Tower Base Access Tunnel 2",
    code=31,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=5)
  ),
  "Tower Base Access Tunnel MD 3": MMXCMLocationData(
    name="Tower Base Access Tunnel 3",
    code=32,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=3)
  ),
  "Tower Base Access Tunnel MD 4": MMXCMLocationData(
    name="Tower Base Access Tunnel 4",
    code=33,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=4)
  ),
  "Equipment Maintenance B MD 1": MMXCMLocationData(
    name="Equipment Maintenance B 1",
    code=34,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=0)
  ),
  "Equipment Maintenance B MD 2": MMXCMLocationData(
    name="Equipment Maintenance B 2",
    code=35, 
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=1)
  ),
  "Equipment Maintenance A MD 1": MMXCMLocationData(
    name="Equipment Maintenance A 1",
    code=36,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=2)
  ),
  "Base Security Station MD 1": MMXCMLocationData(
    name="Base Security Station 1",
    code=37,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=3)
  ),
  "Base Security Station MD 2": MMXCMLocationData(
    name="Base Security Station 2",
    code=38,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=4)
  ),
  "Data Backup Room, Hall A MD 1": MMXCMLocationData(
    name="Data Backup Room, Hall A 1",
    code=39,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=6)
  ),
  "Data Backup Room, Hall A MD 2": MMXCMLocationData(
    name="Data Backup Room, Hall A 2",
    code=40,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=7)
  ),
  "Data Backup Room, Hall B MD 1": MMXCMLocationData(
    name="Data Backup Room, Hall B 1",
    code=41,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2155, bit_position=1)
  ),
  "Command Center Staff Room MD 1": MMXCMLocationData(
    name="Command Center Staff Room 1",
    code=42,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2155, bit_position=2)
  ),
  "Base Entrance MD 1": MMXCMLocationData(
    name="Base Entrance 1",
    code=43,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2155, bit_position=3)
  ),
  "Large Heliport Access Tunnel MD 1": MMXCMLocationData(
    name="Large Heliport Access Tunnel 1",
    code=44,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2155, bit_position=6)
  ),
  "Large Heliport Access Tunnel MD 2": MMXCMLocationData(
    name="Large Heliport Access Tunnel 2",
    code=45,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2155, bit_position=7)
  ),
  "Air City South Square MD 1": MMXCMLocationData(
    name="Air City South Square 1",
    code=46,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=0)
  ),
  "Air City South Square MD 2": MMXCMLocationData(
    name="Air City South Square 2",
    code=47,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=1)
  ),
  "Air City South Square MD 3": MMXCMLocationData(
    name="Air City South Square 3",
    code=48,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=2)
  ),
  "Special Sealed Area First Room MD 1": MMXCMLocationData(
    name="Special Sealed Area 1-4 1",
    code=49,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2148, bit_position=4),
    access_rule=lambda state: state.has("Central Key", 1)
  ),
  "Special Sealed Area First Room MD 2": MMXCMLocationData(
    name="Special Sealed Area 1-4 2",
    code=50,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2148, bit_position=5),
    access_rule=lambda state: state.has("Central Key", 1)
  ),
  "Special Sealed Area First Room MD 3": MMXCMLocationData(
    name="Special Sealed Area 1-4 3",
    code=51,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2148, bit_position=6),
    access_rule=lambda state: state.has("Central Key", 1)
  ),
  "Special Sealed Area First Room MD 4": MMXCMLocationData(
    name="Special Sealed Area 1-4 4",
    code=52,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A2148, bit_position=7),
    access_rule=lambda state: state.has("Central Key", 1)   
  ),
  "Special Sealed Area First Room MD 5": MMXCMLocationData(
    name="Special Sealed Area 1-4 5",
    code=53,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=0),
    access_rule=lambda state: state.has("Central Key", 1)     
  ),
  "Special Sealed Area First Room MD 6": MMXCMLocationData(
    name="Special Sealed Area 1-4 6",
    code=54,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=1),
    access_rule=lambda state: state.has("Central Key", 1)     
  ),
  "Special Sealed Area First Room MD 7": MMXCMLocationData(
    name="Special Sealed Area 1-4 7",
    code=55,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=2),
    access_rule=lambda state: state.has("Central Key", 1) 
  ),
  "Special Sealed Area First Room MD 8": MMXCMLocationData(
    name="Special Sealed Area 1-4 8",
    code=56,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=3),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area First Room MD 9": MMXCMLocationData(
    name="Special Sealed Area 1-4 9",
    code=57,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=4),
    access_rule=lambda state: state.has("Central Key", 1)     
  ),
  "Special Sealed Area 1-4 MD 10": MMXCMLocationData(
    name="Special Sealed Area 1-4 10",
    code=58,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=5),
    access_rule=lambda state: state.has("Central Key", 1)     
  ),
  "Special Sealed Area 2nd Room MD 1": MMXCMLocationData(
    name="Special Sealed Area Second Room 1",
    code=59,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=6),
    access_rule=lambda state: state.has("Central Key", 1)      
  ),
  "Special Sealed Area 2nd Room MD 2": MMXCMLocationData(
    name="Special Sealed Area Second Room 2",
    code=60,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=7),
    access_rule=lambda state: state.has("Central Key", 1)       
  ),
  "Special Sealed Area 2nd Room MD 3": MMXCMLocationData(
    name="Special Sealed Area Second Room 3",
    code=61,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=0),
    access_rule=lambda state: state.has("Central Key", 1)    
  ),
  "Special Sealed Area 2nd Room MD 4": MMXCMLocationData(
    name="Special Sealed Area Second Room 4",
    code=62,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=1),
    access_rule=lambda state: state.has("Central Key", 1)     
  ),
  "Special Sealed Area 2nd Room MD 5": MMXCMLocationData(
    name="Special Sealed Area Second Room 5",
    code=63,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=2),
    access_rule=lambda state: state.has("Central Key", 1)     
  ),
  "Special Sealed Area 2nd Room MD 6": MMXCMLocationData(
    name="Special Sealed Area Second Room 6",
    code=64,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=3),
    access_rule=lambda state: state.has("Central Key", 1)   
  ),
  "Special Sealed Area 2nd Room MD 7": MMXCMLocationData(
    name="Special Sealed Area Second Room 7",
    code=65,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=4),
    access_rule=lambda state: state.has("Central Key", 1)     
  ),
  "Special Sealed Area 2nd Room MD 8": MMXCMLocationData(
    name="Special Sealed Area Second Room 8",
    code=66,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=5),
    access_rule=lambda state: state.has("Central Key", 1)   
  ),
  "Special Sealed Area 2nd Room MD 9": MMXCMLocationData(
    name="Special Sealed Area Second Room 9",
    code=67,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=6),
    access_rule=lambda state: state.has("Central Key", 1)   
  ),
  "Special Sealed Area 2nd Room MD 10": MMXCMLocationData(
    name="Special Sealed Area Second Room 10",
    code=68,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=7),
    access_rule=lambda state: state.has("Central Key", 1)   
  ),
  "Special Sealed Area 3rd Room MD 1": MMXCMLocationData(
    name="Special Sealed Area Third Room 1",
    code=69,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=0),
    access_rule=lambda state: state.has("Central Key", 1)   
  ),
  "Special Sealed Area 3rd Room MD 2": MMXCMLocationData(
    name="Special Sealed Area Third Room 2",
    code=70,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=1),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area 3rd Room MD 3": MMXCMLocationData(
    name="Special Sealed Area Third Room 3",
    code=71,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=2),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area 3rd Room MD 4": MMXCMLocationData(
    name="Special Sealed Area Third Room 4",
    code=72,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=3),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area 3rd Room MD 5": MMXCMLocationData(
    name="Special Sealed Area Third Room 5",
    code=73,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=4),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area 3rd Room MD 6": MMXCMLocationData(
    name="Special Sealed Area Third Room 6",
    code=74,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=5),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area 3rd Room MD 7": MMXCMLocationData(
    name="Special Sealed Area Third Room 7",
    code=75,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=6),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area 3rd Room MD 8": MMXCMLocationData(
    name="Special Sealed Area Third Room 8",
    code=76,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=7),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area By Ninetales MD 1": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 1",
    code=77,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=0),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area By Ninetales MD 2": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 2",
    code=78,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=1),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area By Ninetales MD 3": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 3",
    code=79,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=2),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area By Ninetales MD 4": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 4",
    code=80,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=3),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area By Ninetales MD 5": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 5",
    code=81,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=4),
    access_rule=lambda state: state.has("Central Key", 1)  
  ),
  "Special Sealed Area By Ninetales MD 6": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 6",
    code=82,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=5),
    access_rule=lambda state: state.has("Central Key", 1)
  ),
  "Special Sealed Area By Ninetales MD 7": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 7",
    code=83,
    parent_region="Central Tower",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=6),
    access_rule=lambda state: state.has("Central Key", 1)
  ),
}
# Apply the blanket access rule to all locations that don't have an explicit rule.
for key, data in CENTRAL_TOWER_LOCATIONS.items():
    if data.access_rule is DEFAULT_RULE:
        CENTRAL_TOWER_LOCATIONS[key] = data._replace(
            access_rule=lambda state: state.has("Central Tower Access Code", 1)
        )
   
TIANNA_CAMP_LOCATIONS: dict[str, MMXCMLocationData] = {
  "Security Reploid Patrol Area MD 1": MMXCMLocationData(
    name="Security Reploid Patrol Area 1",
    code=84,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=0)
  ),
  "Security Reploid Patrol Area MD 2": MMXCMLocationData(
    name="Security Reploid Patrol Area 2",
    code=85,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=3)
  ),
  "Security Reploid Patrol Area MD 3": MMXCMLocationData(
    name="Security Reploid Patrol Area 3",
    code=86,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=4)
  ),
  "Security Reploid Patrol Area MD 4": MMXCMLocationData(
    name="Security Reploid Patrol Area 4",
    code=87,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=1)
  ),
  "Security Reploid Patrol Area MD 5": MMXCMLocationData(
    name="Security Reploid Patrol Area 5",
    code=88,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=2)
  ),
  "Prisoner Admission Division MD 1": MMXCMLocationData(
    name="Prisoner Admission Division 1",
    code=89,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=5)
  ),
  "Prisoner Admission Division MD 2": MMXCMLocationData(
    name="Prisoner Admission Division 2",
    code=90,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=6)
  ),
  "Prisoner Admission Division MD 3": MMXCMLocationData(
    name="Prisoner Admission Division 3",
    code=91,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=7)
  ),
  "Prisoner Admission Division MD 4": MMXCMLocationData(
    name="Prisoner Admission Division 4",
    code=92,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215A, bit_position=0)
  ),
  "Main Gate Depth 4 Undersea Prison MD 1": MMXCMLocationData(
    name="Main Gate Depth 4 Undersea Prison 1",
    code=93,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215A, bit_position=1)
  ),
  "East Prison MD 1": MMXCMLocationData(
    name="East Prison 1",
    code=94,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215A, bit_position=2)
  ),
  "East Prison MD 2": MMXCMLocationData(
    name="East Prison 2",
    code=95,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215A, bit_position=3)
  ),
  "West Prison MD 1": MMXCMLocationData(
    name="West Prison 1",
    code=96,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215A, bit_position=5)
  ),
  "West Prison MD 2": MMXCMLocationData(
    name="West Prison 2",
    code=97,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215A, bit_position=6)
  ),
  "Maze Area 1 Behind Key MD 1": MMXCMLocationData(
    name="Maze Area 1 Behind Key 1",
    code=98,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=1),
    access_rule=lambda state: state.has("Tianna Key", 1)
  ),
  "Maze Area 1 MD 2": MMXCMLocationData(
    name="Maze Area 1-2",
    code=99,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=2)
  ),
  "Maze Area 1 MD 3": MMXCMLocationData(
    name="Maze Area 1-3",
    code=100,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=3)
  ),
  "Maze Area 1 MD 4": MMXCMLocationData(
    name="Maze Area 1-4",
    code=101,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=4)
  ),
  "Maze Area 1 MD 5": MMXCMLocationData(
    name="Maze Area 1-5",
    code=102,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=5)
  ),
  "Maze Area 1 Rafflesian MD 1": MMXCMLocationData(
    name="Maze Area 1 Rafflesian 1",
    code=103,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=6),
    access_rule=lambda state: state.has("Tianna Key", 1)
  ),
  "Maze Area 1 Rafflesian MD 2": MMXCMLocationData(
    name="Maze Area 1 Rafflesian 2",
    code=104,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=7),
    access_rule=lambda state: state.has("Tianna Key", 1)
  ),
  "Maze Area 1 Rafflesian MD 3": MMXCMLocationData(
    name="Maze Area 1 Rafflesian 3",
    code=105,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=0),
    access_rule=lambda state: state.has("Tianna Key", 1)
  ),
  "Maze Area 2 MD 1": MMXCMLocationData(
    name="Maze Area 2-1",
    code=106,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=2)    
  ),
  "Maze Area 2 MD 2": MMXCMLocationData(
    name="Maze Area 2-2",
    code=107,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=3)   
  ),
  "Maze Area 2 MD 3": MMXCMLocationData(
    name="Maze Area 2-3",
    code=108,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=4) 
  ),
  "Maze Area 2 MD 4": MMXCMLocationData(
    name="Maze Area 2-4",
    code=109,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=5) 
  ),
  "Maze Area 2 MD 5": MMXCMLocationData(
    name="Maze Area 2-5",
    code=110,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=6) 
  ),
  "Dark Room MD 1": MMXCMLocationData(
    name="Dark Room 1",
    code=111,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=7) 
  ),
  "Security Panel Area MD 1": MMXCMLocationData(
    name="Security Panel Area 1",
    code=112,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=3) 
  ),
  "Security Panel Area MD 2": MMXCMLocationData(
    name="Security Panel Area 2",
    code=113,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=4) 
  ),
  "Security Panel Area MD 3": MMXCMLocationData(
    name="Security Panel Area 3",
    code=114,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=5) 
  ),
  "Security Panel Area MD 4": MMXCMLocationData(
    name="Security Panel Area 4",
    code=115,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=6)
  ),
  "Security Panel Area MD 5": MMXCMLocationData(
    name="Security Panel Area 5",
    code=116,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=7), 
  ),
  "Security Panel Area MD 6": MMXCMLocationData(
    name="Security Panel Area 6",
    code=117,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=1) 
  ),
  "Security Panel Area MD 7": MMXCMLocationData(
    name="Security Panel Area 7",
    code=118,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=0)
  ),
  "Security Panel Area MD 8": MMXCMLocationData(
    name="Security Panel Area 8",
    code=119,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=1) 
  ),
  "Security Panel Area MD 9": MMXCMLocationData(
    name="Security Panel Area 9",
    code=120,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=2) 
  ),
  "Security Panel Area MD 10": MMXCMLocationData(
    name="Security Panel Area 10",
    code=121,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=3) 
  ),
  "Security Panel Area MD 11": MMXCMLocationData(
    name="Security Panel Area 11",
    code=122,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=4) 
  ),
  "Security Panel Area MD 12": MMXCMLocationData(
    name="Security Panel Area 12",
    code=123,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=5) 
  ),
  "Security Panel Area MD 13": MMXCMLocationData(
    name="Security Panel Area 13",
    code=124,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=6)
  ),
  "Security Panel Area MD 14": MMXCMLocationData(
    name="Security Panel Area 14",
    code=125,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=7)
  ),
  "Security Panel Area MD 15": MMXCMLocationData(
    name="Security Panel Area 15",
    code=126,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=2)
  ),
  "Aqua Coliseum Entrance MD 1": MMXCMLocationData(
    name="Aqua Coliseum Entrance 1",
    code=127,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215D, bit_position=1)
  ),
  "Aqua Coliseum Entrance MD 2": MMXCMLocationData(
    name="Aqua Coliseum Entrance 2",
    code=128,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215D, bit_position=2)
  ),
}
# Apply the blanket access rule to all locations that don't have an explicit rule.
for key, data in TIANNA_CAMP_LOCATIONS.items():
    if data.access_rule is DEFAULT_RULE:
        TIANNA_CAMP_LOCATIONS[key] = data._replace(
            access_rule=lambda state: state.has("Tianna Camp Access Code", 1)
        )

GAUDILE_LABORATORY_LOCATIONS: dict[str, MMXCMLocationData] = {
  "East Deck High Speed Lift Area MD 1": MMXCMLocationData(
    name="East Deck High Speed Lift Area 1",
    code=129,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A215C, bit_position=4)
  ),
  "East Deck High Speed Lift Area MD 2": MMXCMLocationData(
    name="East Deck High Speed Lift Area 2",
    code=130,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A215C, bit_position=5)
  ),
  "East Deck High Speed Lift Area MD 3": MMXCMLocationData(
    name="East Deck High Speed Lift Area 3",
    code=131,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A215C, bit_position=6)
  ),
  "East Deck High Speed Lift Area MD 4": MMXCMLocationData(
    name="East Deck High Speed Lift Area 4",
    code=132,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A215C, bit_position=7)
  ),
  "East Deck High Speed Lift Area MD 5": MMXCMLocationData(
    name="East Deck High Speed Lift Area 5",
    code=133,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A215D, bit_position=6)
  ),
  "East Deck Main Route MD 1": MMXCMLocationData(
    name="East Deck Main Route 1",
    code=134,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2163, bit_position=0)
  ),
  "East Deck Main Route MD 2": MMXCMLocationData(
    name="East Deck Main Route 2",
    code=135,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2163, bit_position=1)
  ),
  "East Deck Main Route MD 3": MMXCMLocationData(
    name="East Deck Main Route 3",
    code=136,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2163, bit_position=2)
  ),
  "East Deck Main Route MD 4": MMXCMLocationData(
    name="East Deck Main Route 4",
    code=137,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2163, bit_position=3)
  ),
  "East Deck Residential Division 101 MD 1": MMXCMLocationData(
    name="East Deck Residential Division 101-1",
    code=138,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=4)
  ),
  "East Deck Residential Division 101 MD 2": MMXCMLocationData(
    name="East Deck Residential Division 101-2",
    code=139,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=5)
  ),
  "East Deck Residential Division 101 MD 3": MMXCMLocationData(
    name="East Deck Residential Division 101-3",
    code=140,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=6)
  ),
  "East Deck Residential Division 101 MD 4": MMXCMLocationData(
    name="East Deck Residential Division 101-4",
    code=141,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=7)
  ),
  "East Deck Residential Division 101 MD 5": MMXCMLocationData(
    name="East Deck Residential Division 101-5",
    code=142,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=0)
  ),
  "East Deck Residential Division 102 MD 1": MMXCMLocationData(
    name="East Deck Residential Division 102-1",
    code=143,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=1)
  ),
  "East Deck Residential Division 102 MD 2": MMXCMLocationData(
    name="East Deck Residential Division 102-2",
    code=144,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=2)
  ),
  "East Deck Residential Division 102 MD 3": MMXCMLocationData(
    name="East Deck Residential Division 102-3",
    code=145,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=3)
  ),
  "East Deck Residential Division 102 MD 4": MMXCMLocationData(
    name="East Deck Residential Division 102-4",
    code=146,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=4)
  ),
  "Observation Deck Area MD 1": MMXCMLocationData(
    name="Observation Deck Area 1",
    code=147,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2162, bit_position=0)
  ),
  "Observation Deck Area MD 2": MMXCMLocationData(
    name="Observation Deck Area 2",
    code=148,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2162, bit_position=1)
  ),
  "Observation Deck Area MD 3": MMXCMLocationData(
    name="Observation Deck Area 3",
    code=149,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2163, bit_position=6)
  ),
  "Observation Deck Area MD 4": MMXCMLocationData(
    name="Observation Deck Area 4",
    code=150,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2163, bit_position=7)
  ),
  "Laboratory Approach MD 1": MMXCMLocationData(
    name="Laboratory Approach 1",
    code=151,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2162, bit_position=4)
  ),
  "Laboratory Approach MD 2": MMXCMLocationData(
    name="Laboratory Approach 2",
    code=152,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2162, bit_position=5)
  ),
  "Laboratory Approach MD 3": MMXCMLocationData(
    name="Laboratory Approach 3",
    code=153,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2162, bit_position=6)
  ),
  "Counter-Biohazard Sample Storage MD 1": MMXCMLocationData(
    name="Counter-Biohazard Sample Storage 1",
    code=154,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2161, bit_position=0)
  ),
  "Counter-Biohazard Sample Storage MD 2": MMXCMLocationData(
    name="Counter-Biohazard Sample Storage 2",
    code=155,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2161, bit_position=1)
  ),
  "Counter-Biohazard Sample Storage MD 3": MMXCMLocationData(
    name="Counter-Biohazard Sample Storage 3",
    code=156,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2161, bit_position=2)
  ),
  "Counter-Biohazard Sample Storage MD 4": MMXCMLocationData(
    name="Counter-Biohazard Sample Storage 4",
    code=157,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2161, bit_position=3)
  ),
  "Counter-Biohazard Sample Storage MD 5": MMXCMLocationData(
    name="Counter-Biohazard Sample Storage 5",
    code=158,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2161, bit_position=4)
  ),
  "West Deck Main Route MD 1": MMXCMLocationData(
    name="West Deck Main Route 1",
    code=159,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=0)
  ),
  "West Deck Main Route MD 2": MMXCMLocationData(
    name="West Deck Main Route 2",
    code=160,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=1)
  ),
  "West Deck Main Route MD 3": MMXCMLocationData(
    name="West Deck Main Route 3",
    code=161,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=2)
  ),
  "Great Tree Stump Hall Approach MD 1": MMXCMLocationData(
    name="Great Tree Stump Hall Approach 1",
    code=162,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=5)
  ),
  "Great Tree Stump Hall Approach MD 2": MMXCMLocationData(
    name="Great Tree Stump Hall Approach 2",
    code=163,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=6)
  ),  
}
# Apply the blanket access rule to all locations that don't have an explicit rule.
for key, data in GAUDILE_LABORATORY_LOCATIONS.items():
    if data.access_rule is DEFAULT_RULE:
        GAUDILE_LABORATORY_LOCATIONS[key] = data._replace(
            access_rule=lambda state: state.has("Gaudile Laboratory Access Code", 1)
        )
      
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
    
