from typing import NamedTuple, Dict, Optional, Callable
from . import items
from .helpers import MMXCMRamData

# This will list the exact blueprint for making our locations!
class MMXCMLocationData(NamedTuple):
  name:str
  code:Optional[int]
  parent_region: str
  ram_addr: Optional[MMXCMRamData] = None
  event_item: bool = False

# These are the static locations we can't get from the server but are still considered "locations".
REBELLION_MEDALS_DATA: Dict[str, Dict[str, any]] = {
    "Rebellion Medal 1": {
        "ram_addr": MMXCMRamData(0x804A2109, bit_position=2)
    },
    "Rebellion Medal 2": {
        "ram_addr": MMXCMRamData(0x804A2109, bit_position=3)
    },
    "Rebellion Medal 3": {
        "ram_addr": MMXCMRamData(0x804A2109, bit_position=4)
    },
    "Rebellion Medal 4": {
        "ram_addr": MMXCMRamData(0x804A2109, bit_position=5)
    },
    "Rebellion Medal 5": {
        "ram_addr": MMXCMRamData(0x804A2109, bit_position=6)
    },
    "Rebellion Medal 6": {
        "ram_addr": MMXCMRamData(0x804A2109, bit_position=7)
    },
    "Rebellion Medal 7": {
        "ram_addr": MMXCMRamData(0x804A210A, bit_position=0)
    },
    "Rebellion Medal 8": {
        "ram_addr": MMXCMRamData(0x804A210A, bit_position=1)
    },
    "Rebellion Medal 9": {
        "ram_addr": MMXCMRamData(0x804A210A, bit_position=2)
    },
}

# This begins the list for every single randomized item in AP.
LAGRANO_RUINS_LOCATIONS: dict[str, MMXCMLocationData] = {
  # Here is an example of the location and the bit position to track it.
  "Area 1F East 50z": MMXCMLocationData(
    name="Area 1F East 1",
    code=1,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x804A2153, bit_position=2)
  ),
  "Area 1F East Build LE": MMXCMLocationData(
    name="Area 1F East 2", 
    code=2,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x804A2153, bit_position=3)
  ),
  "Area 2F East Tank Energy 25": MMXCMLocationData(
    name="Area 2F East 1",
    code=3,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x804A2153, bit_position=5)
  ),
  "Area 2F East Anti-Lock": MMXCMLocationData(
    name="Area 2F East 2",
    code=4,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x804A2153, bit_position=6)
  ),
  "Area 2F East 50z": MMXCMLocationData(
    name="Area 2F East 3",
    code=5,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x804A2153, bit_position=7)
  ),
  "Area 2F East 70z": MMXCMLocationData(
    name="Area 2F East 4",
    code=6,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=0)
  ),
  "Area 3F East Tank Energy 25": MMXCMLocationData(
    name="Area 3F East 1",
    code=7,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=3)
  ),
  "Area 3F East Melt Missile": MMXCMLocationData(
    name="Area 3F East 2",
    code=8,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=2)
  ),
  "East Area Stairs 3F to 4F Tank Energy 50": MMXCMLocationData(
    name="East Area Stairs 3F to 4F 1",
    code=9,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=4)
  ),
  "Area 4F East Backup": MMXCMLocationData(
    name="Area 4F East 1",
    code=10,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=3)
  ),
  "Area 4F East Build Shield": MMXCMLocationData(
    name="Area 4F East 2",
    code=11,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=2)
  ),
  "Area 4F East Tank Energy Infinite": MMXCMLocationData(
    name="Area 4F East 3",
    code=12,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=1)
  ),
  "4F: Test Hall 1 Power +1": MMXCMLocationData(
  # These two entries are the MD's after Hippo is defeated.
    name="4F Test Hall 1-1",
    code=13,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=0)
  ),
  "4F: Test Hall 1 Speed +1": MMXCMLocationData(
    name="4F Test Hall 1-2",
    code=14,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=7)
  ),
  "Area 4F West Tank Parts": MMXCMLocationData(
    name="Area 4F West 1",
    code=15,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=6)
  ),
  "Area 4F West 80z": MMXCMLocationData(
    name="Area 4F West 2",
    code=16,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042152, bit_position=5)
  ), 
  "East Area Stairs 4F to 5F Tank Parts": MMXCMLocationData(
    name="East Area Stairs 4F to 5F MD 1",
    code=17,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=5)
  ),
  "East Area Stairs 4F to 5F Figure Token 1": MMXCMLocationData(
    name="East Area Stairs 4F to 5F 2",
    code=18,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=6)
  ),      
  "East Area Stairs 4F to 5F Figure Token 2": MMXCMLocationData(
    name="East Area Stairs 4F to 5F 3",
    code=19,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042151, bit_position=7)
  ),
  "Area 5F West Reboot": MMXCMLocationData(
    name="Area 5F West 1",
    code=20,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042150, bit_position=0)
  ),
  "Area 5F West Vaccine Program": MMXCMLocationData(
    name="Area 5F West 2",
    code=21,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x8042150, bit_position=1)
  ), 
}
          
# Location tables for other regions as they are filled. 
CENTRAL_TOWER_LOCATIONS: dict[str, MMXCMLocationData] = {
  "Shaft 999F Clear Vision": MMXCMLocationData(
    name="Shaft 999F 1",
    code=22,
    parent_region="Central Tower Hub",
    ram_addr=MMXCMRamData(0x804A2150, bit_position=6)
  ),
  "Shaft 999F Vaccine Program": MMXCMLocationData(
    name="Shaft 999F 2",
    code=23,
    parent_region="Central Tower Hub",
    ram_addr=MMXCMRamData(0x804A2150, bit_position=4)
  ),
  "Shaft 999F Build Power": MMXCMLocationData(
    name="Shaft 999F 3",
    code=24,
    parent_region="Central Tower Hub",
    ram_addr=MMXCMRamData(0x804A2150, bit_position=5)
  ),
  "Access Tunnel E-1 East Gain Hyper": MMXCMLocationData(
    name="Access Tunnel E-1 East 1",
    code=25,
    parent_region="Central Tower Hub",
    ram_addr=MMXCMRamData(0x804A2154, bit_position=4)
  ),
  "Access Tunnel E-1 East Tank Energy 100": MMXCMLocationData(
    name="Access Tunnel E-1 East 2",
    code=26,
    parent_region="Central Tower Hub",
    ram_addr=MMXCMRamData(0x804A2154, bit_position=5)
  ),
  "Access Tunnel E-1 North Power Charge": MMXCMLocationData(
    name="Access Tunnel E-1 North 1",
    code=27,
    parent_region="Central Tower Hub",
    ram_addr=MMXCMRamData(0x804A2154, bit_position=2)
  ),
  "Access Tunnel E-1 North Tank Energy 50": MMXCMLocationData(
    name="Access Tunnel E-1 North 2",
    code=28,
    parent_region="Central Tower Hub",
    ram_addr=MMXCMRamData(0x804A2154, bit_position=3)
  ),
  "Access Tunnel E-1 North 100z": MMXCMLocationData(
    name="Access Tunnel E-1 North 3",
    code=29,
    parent_region="Central Tower Hub",
    ram_addr=MMXCMRamData(0x804A2154, bit_position=6)
  ),
  "Tower Base Access Tunnel Gain Hyper": MMXCMLocationData(
    name="Tower Base Access Tunnel 1",
    code=30,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=6)
  ),
  "Tower Base Access Tunnel Mega Fire": MMXCMLocationData(
    name="Tower Base Access Tunnel 2",
    code=31,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=5)
  ),
  "Tower Base Access Tunnel 100z": MMXCMLocationData(
    name="Tower Base Access Tunnel 3",
    code=32,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=3)
  ),
  "Tower Base Access Tunnel Tank Energy Infinite": MMXCMLocationData(
    name="Tower Base Access Tunnel 4",
    code=33,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=4)
  ),
  "Equipment Maintenance B Build Armor": MMXCMLocationData(
    name="Equipment Maintenance B 1",
    code=34,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=0)
  ),
  "Equipment Maintenance B Build Speed": MMXCMLocationData(
    name="Equipment Maintenance B 2",
    code=35, 
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=1)
  ),
  "Equipment Maintenance A 100z": MMXCMLocationData(
    name="Equipment Maintenance A 1",
    code=36,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=2)
  ),
  "Base Security Station 200z": MMXCMLocationData(
    name="Base Security Station 1",
    code=37,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=3)
  ),
  "Base Security Station Ultra Fire": MMXCMLocationData(
    name="Base Security Station 2",
    code=38,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=4)
  ),
  "Data Backup Room, Hall A Tank Energy 50": MMXCMLocationData(
    name="Data Backup Room, Hall A 1",
    code=39,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=6)
  ),
  "Data Backup Room, Hall A Eagle Eye": MMXCMLocationData(
    name="Data Backup Room, Hall A 2",
    code=40,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2156, bit_position=7)
  ),
  "Data Backup Room, Hall B 100z": MMXCMLocationData(
    name="Data Backup Room, Hall B 1",
    code=41,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2155, bit_position=1)
  ),
  "Command Center Staff Room Tank Parts": MMXCMLocationData(
    name="Command Center Staff Room 1",
    code=42,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2155, bit_position=2)
  ),
  "Base Entrance Tank Energy 25": MMXCMLocationData(
    name="Base Entrance 1",
    code=43,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2155, bit_position=3)
  ),
  "Large Heliport Access Tunnel Tank Energy 100": MMXCMLocationData(
    name="Large Heliport Access Tunnel 1",
    code=44,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2155, bit_position=6)
  ),
  "Large Heliport Access Tunnel Backup": MMXCMLocationData(
    name="Large Heliport Access Tunnel 2",
    code=45,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2155, bit_position=7)
  ),
  "Air City South Square Figure Token 1": MMXCMLocationData(
    name="Air City South Square 1",
    code=46,
    parent_region="Central Tower Hub",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=0)
  ),
  "Air City South Square Figure Token 2": MMXCMLocationData(
    name="Air City South Square 2",
    code=47,
    parent_region="Central Tower Hub",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=1)
  ),
  "Air City South Square Figure Token 3": MMXCMLocationData(
    name="Air City South Square 3",
    code=48,
    parent_region="Central Tower Hub",
    ram_addr=MMXCMRamData(0x804A2157, bit_position=2)
  ),
  "Special Sealed Area 1st Room Enter The Intruder": MMXCMLocationData(
    name="Special Sealed Area 1-4 1",
    code=49,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2148, bit_position=4)
  ),
  "Special Sealed Area 1st Room The Throne": MMXCMLocationData(
    name="Special Sealed Area 1-4 2",
    code=50,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2148, bit_position=5)
  ),
  "Special Sealed Area 1st Room Capital": MMXCMLocationData(
    name="Special Sealed Area 1-4 3",
    code=51,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2148, bit_position=6)
  ),
  "Special Sealed Area 1st Room Battle Epsilon": MMXCMLocationData(
    name="Special Sealed Area 1-4 4",
    code=52,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A2148, bit_position=7)
  ),
  "Special Sealed Area 1st Room Epsilon 1": MMXCMLocationData(
    name="Special Sealed Area 1-4 5",
    code=53,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=0)
  ),
  "Special Sealed Area 1st Room Ruins Passageway": MMXCMLocationData(
    name="Special Sealed Area 1-4 6",
    code=54,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=1)     
  ),
  "Special Sealed Area 1st Room The End": MMXCMLocationData(
    name="Special Sealed Area 1-4 7",
    code=55,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=2)
  ),
  "Special Sealed Area 1st Room Epsilon 2": MMXCMLocationData(
    name="Special Sealed Area 1-4 8",
    code=56,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=3) 
  ),
  "Special Sealed Area 1st Room Display Device": MMXCMLocationData(
    name="Special Sealed Area 1-4 9",
    code=57,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=4)    
  ),
  "Special Sealed Area 1st Room Grave Ruins": MMXCMLocationData(
    name="Special Sealed Area 1-4 10",
    code=58,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=5) 
  ),
  "Special Sealed Area 2nd Room Flying Mechs": MMXCMLocationData(
    name="Special Sealed Area Second Room 1",
    code=59,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=6)
  ),
  "Special Sealed Area 2nd Room Redips Soldier": MMXCMLocationData(
    name="Special Sealed Area Second Room 2",
    code=60,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214F, bit_position=7)
  ),
  "Special Sealed Area 2nd Room Aerial Assault": MMXCMLocationData(
    name="Special Sealed Area Second Room 3",
    code=61,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=0)
  ),
  "Special Sealed Area 2nd Room Dragoon": MMXCMLocationData(
    name="Special Sealed Area Second Room 4",
    code=62,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=1)  
  ),
  "Special Sealed Area 2nd Room The Chair": MMXCMLocationData(
    name="Special Sealed Area Second Room 5",
    code=63,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=2)  
  ),
  "Special Sealed Area 2nd Room Transform Ability": MMXCMLocationData(
    name="Special Sealed Area Second Room 6",
    code=64,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=3)  
  ),
  "Special Sealed Area 2nd Room Transforming Mech": MMXCMLocationData(
    name="Special Sealed Area Second Room 7",
    code=65,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=4)
  ),
  "Special Sealed Area 2nd Room Coliseum": MMXCMLocationData(
    name="Special Sealed Area Second Room 8",
    code=66,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=5)  
  ),
  "Special Sealed Area 2nd Room Battle Redips": MMXCMLocationData(
    name="Special Sealed Area Second Room 9",
    code=67,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=6) 
  ),
  "Special Sealed Area 2nd Room Judgment": MMXCMLocationData(
    name="Special Sealed Area Second Room 10",
    code=68,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214E, bit_position=7)
  ),
  "Special Sealed Area 3rd Room Redips 1": MMXCMLocationData(
    name="Special Sealed Area Third Room 1",
    code=69,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=0)
  ),
  "Special Sealed Area 3rd Room Space": MMXCMLocationData(
    name="Special Sealed Area Third Room 2",
    code=70,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=1)
  ),
  "Special Sealed Area 3rd Room Epsilon": MMXCMLocationData(
    name="Special Sealed Area Third Room 3",
    code=71,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=2)
  ),
  "Special Sealed Area 3rd Room Redips 2": MMXCMLocationData(
    name="Special Sealed Area Third Room 4",
    code=72,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=3)
  ),
  "Special Sealed Area 3rd Room Redips 3": MMXCMLocationData(
    name="Special Sealed Area Third Room 5",
    code=73,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=4)
  ),
  "Special Sealed Area 3rd Room Tails": MMXCMLocationData(
    name="Special Sealed Area Third Room 6",
    code=74,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=5) 
  ),
  "Special Sealed Area 3rd Room Parts": MMXCMLocationData(
    name="Special Sealed Area Third Room 7",
    code=75,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=6)
  ),
  "Special Sealed Area 3rd Room Scores Settled": MMXCMLocationData(
    name="Special Sealed Area Third Room 8",
    code=76,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214D, bit_position=7)
  ),
  "Special Sealed Area By Ninetales Great Redips": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 1",
    code=77,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=0) 
  ),
  "Special Sealed Area By Ninetales Tails Front": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 2",
    code=78,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=1)
  ),
  "Special Sealed Area By Ninetales Tails Back": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 3",
    code=79,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=2) 
  ),
  "Special Sealed Area By Ninetales X's Weapons": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 4",
    code=80,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=3)
  ),
  "Special Sealed Area By Ninetales Zero's Weapons": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 5",
    code=81,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=4)
  ),
  "Special Sealed Area By Ninetales Cinnamon's Weapons": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 6",
    code=82,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=5)
  ),
  "Special Sealed Area By Ninetales Massimo's Weapons": MMXCMLocationData(
    name="Special Sealed Area By Ninetales 7",
    code=83,
    parent_region="Central Tower Full",
    ram_addr=MMXCMRamData(0x804A214C, bit_position=6)
  ),
}
   
TIANNA_CAMP_LOCATIONS: dict[str, MMXCMLocationData] = {
  "Security Reploid Patrol Area Figure Token 1": MMXCMLocationData(
    name="Security Reploid Patrol Area 1",
    code=84,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=0)
  ),
  "Security Reploid Patrol Area 300z": MMXCMLocationData(
    name="Security Reploid Patrol Area 2",
    code=85,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=3)
  ),
  "Security Reploid Patrol Area Figure Token 2": MMXCMLocationData(
    name="Security Reploid Patrol Area 3",
    code=86,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=4)
  ),
  "Security Reploid Patrol Area Decoy": MMXCMLocationData(
    name="Security Reploid Patrol Area 4",
    code=87,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=1)
  ),
  "Security Reploid Patrol Area Thunder Missile": MMXCMLocationData(
    name="Security Reploid Patrol Area 5",
    code=88,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=2)
  ),
  "Prisoner Admission Division Mega Thunder": MMXCMLocationData(
    name="Prisoner Admission Division 1",
    code=89,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=5)
  ),
  "Prisoner Admission Division Build Speed": MMXCMLocationData(
    name="Prisoner Admission Division 2",
    code=90,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=6)
  ),
  "Prisoner Admission Division Boost Armor": MMXCMLocationData(
    name="Prisoner Admission Division 3",
    code=91,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215B, bit_position=7)
  ),
  "Prisoner Admission Division Figure Token": MMXCMLocationData(
    name="Prisoner Admission Division 4",
    code=92,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215A, bit_position=0)
  ),
  "Main Gate Depth 4 Undersea Prison Tank Energy 100": MMXCMLocationData(
    name="Main Gate Depth 4 Undersea Prison 1",
    code=93,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215A, bit_position=1)
  ),
  "East Prison 400z": MMXCMLocationData(
    name="East Prison 1",
    code=94,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215A, bit_position=2)
  ),
  "East Prison Figure Token": MMXCMLocationData(
    name="East Prison 2",
    code=95,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215A, bit_position=3)
  ),
  "West Prison Reboot": MMXCMLocationData(
    name="West Prison 1",
    code=96,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215A, bit_position=5)
  ),
  "West Prison Jack of Hearts": MMXCMLocationData(
    name="West Prison 2",
    code=97,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215A, bit_position=6)
  ),
  "Maze Area 1 Behind Key Tank Parts": MMXCMLocationData(
    name="Maze Area 1 Behind Key 1",
    code=98,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=1)
  ),
  "Maze Area 1 Build Armor": MMXCMLocationData(
    name="Maze Area 1-2",
    code=99,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=2)
  ),
  "Maze Area 1 Build Shield": MMXCMLocationData(
    name="Maze Area 1-3",
    code=100,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=3)
  ),
  "Maze Area 1 Tank Energy 50": MMXCMLocationData(
    name="Maze Area 1-4",
    code=101,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=4)
  ),
  "Maze Area 1 200z": MMXCMLocationData(
    name="Maze Area 1-5",
    code=102,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=5)
  ),
  "Maze Area 1 Rafflesian Figure Token 1": MMXCMLocationData(
    name="Maze Area 1 Rafflesian 1",
    code=103,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=6)
  ),
  "Maze Area 1 Rafflesian Figure Token 2": MMXCMLocationData(
    name="Maze Area 1 Rafflesian 2",
    code=104,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2159, bit_position=7)
  ),
  "Maze Area 1 Rafflesian Ultimate Armor": MMXCMLocationData(
    name="Maze Area 1 Rafflesian 3",
    code=105,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=0)
  ),
  "Maze Area 2 Tank Energy 50": MMXCMLocationData(
    name="Maze Area 2-1",
    code=106,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=2)    
  ),
  "Maze Area 2 Tomahawk": MMXCMLocationData(
    name="Maze Area 2-2",
    code=107,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=3)   
  ),
  "Maze Area 2 Warm-up": MMXCMLocationData(
    name="Maze Area 2-3",
    code=108,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=4) 
  ),
  "Maze Area 2 Boost Power": MMXCMLocationData(
    name="Maze Area 2-4",
    code=109,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=5) 
  ),
  "Maze Area 2 Boost Shield": MMXCMLocationData(
    name="Maze Area 2-5",
    code=110,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=6) 
  ),
  "Dark Room Tank Energy 50": MMXCMLocationData(
    name="Dark Room 1",
    code=111,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A2158, bit_position=7) 
  ),
  "Security Panel Area Build LE": MMXCMLocationData(
    name="Security Panel Area 1",
    code=112,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=3) 
  ),
  "Security Panel Area Build Power": MMXCMLocationData(
    name="Security Panel Area 2",
    code=113,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=4) 
  ),
  "Security Panel Area Build Armor": MMXCMLocationData(
    name="Security Panel Area 3",
    code=114,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=5) 
  ),
  "Security Panel Area Build Shield": MMXCMLocationData(
    name="Security Panel Area 4",
    code=115,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=6)
  ),
  "Security Panel Area Build Speed": MMXCMLocationData(
    name="Security Panel Area 5",
    code=116,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=7), 
  ),
  "Security Panel Area Tank Parts": MMXCMLocationData(
    name="Security Panel Area 6",
    code=117,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=1) 
  ),
  "Security Panel Area Figure Token 1": MMXCMLocationData(
    name="Security Panel Area 7",
    code=118,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=0)
  ),
  "Security Panel Area Figure Token 2": MMXCMLocationData(
    name="Security Panel Area 8",
    code=119,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=1) 
  ),
  "Security Panel Area Figure Token 3": MMXCMLocationData(
    name="Security Panel Area 9",
    code=120,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=2) 
  ),
  "Security Panel Area Figure Token 4": MMXCMLocationData(
    name="Security Panel Area 10",
    code=121,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=3) 
  ),
  "Security Panel Area 400z": MMXCMLocationData(
    name="Security Panel Area 11",
    code=122,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=4) 
  ),
  "Security Panel Area 300z": MMXCMLocationData(
    name="Security Panel Area 12",
    code=123,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=5) 
  ),
  "Security Panel Area 200z": MMXCMLocationData(
    name="Security Panel Area 13",
    code=124,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=6)
  ),
  "Security Panel Area 100z": MMXCMLocationData(
    name="Security Panel Area 14",
    code=125,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215E, bit_position=7)
  ),
  "Security Panel Area Queen of Diamonds": MMXCMLocationData(
    name="Security Panel Area 15",
    code=126,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215F, bit_position=2)
  ),
  "Aqua Coliseum Entrance Gain Hyper": MMXCMLocationData(
    name="Aqua Coliseum Entrance 1",
    code=127,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215D, bit_position=1)
  ),
  "Aqua Coliseum Entrance Tank Energy 100": MMXCMLocationData(
    name="Aqua Coliseum Entrance 2",
    code=128,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A215D, bit_position=2)
  ),
}

GAUDILE_LABORATORY_LOCATIONS: dict[str, MMXCMLocationData] = {
  "East Deck High Speed Lift Area Cooler": MMXCMLocationData(
    name="East Deck High Speed Lift Area 1",
    code=129,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A215C, bit_position=4)
  ),
  "East Deck High Speed Lift Area Vaccine Program": MMXCMLocationData(
    name="East Deck High Speed Lift Area 2",
    code=130,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A215C, bit_position=5)
  ),
  "East Deck High Speed Lift Area Figure Token 1": MMXCMLocationData(
    name="East Deck High Speed Lift Area 3",
    code=131,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A215C, bit_position=6)
  ),
  "East Deck High Speed Lift Area Figure Token 2": MMXCMLocationData(
    name="East Deck High Speed Lift Area 4",
    code=132,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A215C, bit_position=7)
  ),
  "East Deck High Speed Lift Area Cure One": MMXCMLocationData(
    name="East Deck High Speed Lift Area 5",
    code=133,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A215D, bit_position=6)
  ),
  "East Deck Main Route Tank Energy 25": MMXCMLocationData(
    name="East Deck Main Route 1",
    code=134,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2163, bit_position=0)
  ),
  "East Deck Main Route LE +100": MMXCMLocationData(
    name="East Deck Main Route 2",
    code=135,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2163, bit_position=1)
  ),
  "East Deck Main Route Build WE": MMXCMLocationData(
    name="East Deck Main Route 3",
    code=136,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2163, bit_position=2)
  ),
  "East Deck Main Route Build LE": MMXCMLocationData(
    name="East Deck Main Route 4",
    code=137,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2163, bit_position=3)
  ),
  "East Deck Residential Division 101 Figure Token 1": MMXCMLocationData(
    name="East Deck Residential Division 101-1",
    code=138,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=4)
  ),
  "East Deck Residential Division 101 Figure Token 2": MMXCMLocationData(
    name="East Deck Residential Division 101-2",
    code=139,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=5)
  ),
  "East Deck Residential Division 101 Figure Token 3": MMXCMLocationData(
    name="East Deck Residential Division 101-3",
    code=140,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=6)
  ),
  "East Deck Residential Division 101 Figure Token 4": MMXCMLocationData(
    name="East Deck Residential Division 101-4",
    code=141,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=7)
  ),
  "East Deck Residential Division 101 Figure Token 5": MMXCMLocationData(
    name="East Deck Residential Division 101-5",
    code=142,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=0)
  ),
  "East Deck Residential Division 102 Tank Parts": MMXCMLocationData(
    name="East Deck Residential Division 102-1",
    code=143,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=1)
  ),
  "East Deck Residential Division 102 600z": MMXCMLocationData(
    name="East Deck Residential Division 102-2",
    code=144,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=2)
  ),
  "East Deck Residential Division 102 Protect +1": MMXCMLocationData(
    name="East Deck Residential Division 102-3",
    code=145,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=3)
  ),
  "East Deck Residential Division 102 Tank Energy 50": MMXCMLocationData(
    name="East Deck Residential Division 102-4",
    code=146,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=4)
  ),
  "Observation Deck Area Figure Token 1": MMXCMLocationData(
    name="Observation Deck Area 1",
    code=147,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2162, bit_position=0)
  ),
  "Observation Deck Area Tank Energy 50": MMXCMLocationData(
    name="Observation Deck Area 2",
    code=148,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2162, bit_position=1)
  ),
  "Observation Deck Area Figure Token 2": MMXCMLocationData(
    name="Observation Deck Area 3",
    code=149,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2163, bit_position=6)
  ),
  "Observation Deck Area Queen of Hearts": MMXCMLocationData(
    name="Observation Deck Area 4",
    code=150,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2163, bit_position=7)
  ),
  "Laboratory Approach Cure All": MMXCMLocationData(
    name="Laboratory Approach 1",
    code=151,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2162, bit_position=4)
  ),
  "Laboratory Approach 500z 1": MMXCMLocationData(
    name="Laboratory Approach 2",
    code=152,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2162, bit_position=5)
  ),
  "Laboratory Approach 500z 2": MMXCMLocationData(
    name="Laboratory Approach 3",
    code=153,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2162, bit_position=6)
  ),
  "Counter-Biohazard Sample Storage Build Armor": MMXCMLocationData(
    name="Counter-Biohazard Sample Storage 1",
    code=154,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2161, bit_position=0)
  ),
  "Counter-Biohazard Sample Storage Build Speed": MMXCMLocationData(
    name="Counter-Biohazard Sample Storage 2",
    code=155,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2161, bit_position=1)
  ),
  "Counter-Biohazard Sample Storage Gain WE+5": MMXCMLocationData(
    name="Counter-Biohazard Sample Storage 3",
    code=156,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2161, bit_position=2)
  ),
  "Counter-Biohazard Sample Storage Figure Token 1": MMXCMLocationData(
    name="Counter-Biohazard Sample Storage 4",
    code=157,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2161, bit_position=3)
  ),
  "Counter-Biohazard Sample Storage Figure Token 2": MMXCMLocationData(
    name="Counter-Biohazard Sample Storage 5",
    code=158,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2161, bit_position=4)
  ),
  "West Deck Main Route Cure One": MMXCMLocationData(
    name="West Deck Main Route 1",
    code=159,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=0)
  ),
  "West Deck Main Route Reboot": MMXCMLocationData(
    name="West Deck Main Route 2",
    code=160,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=1)
  ),
  "West Deck Main Route Tank Energy 50": MMXCMLocationData(
    name="West Deck Main Route 3",
    code=161,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2160, bit_position=2)
  ),
  "Great Tree Stump Hall Approach Tank Energy 100": MMXCMLocationData(
    name="Great Tree Stump Hall Approach 1",
    code=162,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=5)
  ),
  "Great Tree Stump Hall Approach Gain Hyper": MMXCMLocationData(
    name="Great Tree Stump Hall Approach 2",
    code=163,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A2167, bit_position=6)
  ),  
}
      
ULFAT_FACTORY_LOCATIONS: dict[str, MMXCMLocationData] = {
  "Smelting Furnace 1 300 FME": MMXCMLocationData(
    name="Smelting Furnace 1-1",
    code=164,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2166, bit_position=0)
  ),
  "Smelting Furnace 1 1000z": MMXCMLocationData(
    name="Smelting Furnace 1-2",
    code=165,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2166, bit_position=1)
  ),
  "Smelting Furnace 1 Fire Guard": MMXCMLocationData(
    name="Smelting Furnace 1-3",
    code=166,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2166, bit_position=2)
  ),
  "Smelting Furnace 1 Ultra Blizzard": MMXCMLocationData(
    name="Smelting Furnace 1-4",
    code=167,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2166, bit_position=3)
  ),
  "Smelting Furnace 1 Build LE": MMXCMLocationData(
    name="Smelting Furnace 1-5",
    code=168,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2166, bit_position=4)
  ),
  "Smelting Furnace 1 Figure Token 1": MMXCMLocationData(
    name="Smelting Furnace 1-6",
    code=169,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2166, bit_position=5)
  ),
  "Smelting Furnace 1 Figure Token 2": MMXCMLocationData(
    name="Smelting Furnace 1-7",
    code=170,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2166, bit_position=6)
  ),
  "Smelting Furnace 2 Tank Parts": MMXCMLocationData(
    name="Smelting Furnace 2-1",
    code=171,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2165, bit_position=0)
  ),
  "Smelting Furnace 2 King of Hearts": MMXCMLocationData(
    name="Smelting Furnace 2-2",
    code=172,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2165, bit_position=1)
  ),
  "Smelting Furnace 2 Figure Token 1": MMXCMLocationData(
    name="Smelting Furnace 2-3",
    code=173,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2165, bit_position=2)
  ),
  "Smelting Furnace 2 Build WE": MMXCMLocationData(
    name="Smelting Furnace 2-4",
    code=174,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2165, bit_position=3)
  ),
  "Smelting Furnace 2 Tank Energy 50": MMXCMLocationData(
    name="Smelting Furnace 2-5",
    code=175,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2165, bit_position=4)
  ),
  "Smelting Furnace 2 800z": MMXCMLocationData(
    name="Smelting Furnace 2-6",
    code=176,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2165, bit_position=5)
  ),
  "Smelting Furnace 2 Figure Token 2": MMXCMLocationData(
    name="Smelting Furnace 2-7",
    code=177,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2165, bit_position=6)
  ),
  "Smelting Furnace 3 Mini Battery": MMXCMLocationData(
    name="Smelting Furnace 3-1",
    code=178,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2164, bit_position=0)
  ),
  "Smelting Furnace 3 Aero Buster": MMXCMLocationData(
    name="Smelting Furnace 3-2",
    code=179,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2164, bit_position=1)
  ),
  "Smelting Furnace 3 Tank Energy 50": MMXCMLocationData(
    name="Smelting Furnace 3-3",
    code=180,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2164, bit_position=2)
  ),
  "Smelting Furnace 3 Boost Speed": MMXCMLocationData(
    name="Smelting Furnace 3-4",
    code=181,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2164, bit_position=3)
  ),
  "Smelting Furnace 3 Build Speed": MMXCMLocationData(
    name="Smelting Furnace 3-5",
    code=182,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2164, bit_position=4)
  ),
  "Parts Intake Line Gain Hyper": MMXCMLocationData(
    name="Parts Intake Line 1",
    code=183,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2164, bit_position=6)
  ),
  "Parts Intake Line Tank Energy 25": MMXCMLocationData(
    name="Parts Intake Line 2",
    code=184,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2164, bit_position=7)
  ),
  "Parts Intake Line 1000z": MMXCMLocationData(
    name="Parts Intake Line 3",
    code=185,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A216B, bit_position=0)
  ),
  "Parts Intake Line WE +5": MMXCMLocationData(
    name="Parts Intake Line 4",
    code=186,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A216B, bit_position=1)
  ),
  "Parts Delivery Line Figure Token 1": MMXCMLocationData(
    name="Parts Delivery Line 1",
    code=187,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A216B, bit_position=5)
  ),
  "Parts Delivery Line Figure Token 2": MMXCMLocationData(
    name="Parts Delivery Line 2",
    code=188,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A216B, bit_position=6)
  ),
  "Parts Delivery Line Figure Token 3": MMXCMLocationData(
    name="Parts Delivery Line 3",
    code=189,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A216B, bit_position=7)
  ),
  "Parts Delivery Line Figure Token 4": MMXCMLocationData(
    name="Parts Delivery Line 4",
    code=190,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A216A, bit_position=0)
  ),
  "Parts Delivery Line Figure Token 5": MMXCMLocationData(
    name="Parts Delivery Line 5",
    code=191,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A216A, bit_position=1)
  ),
  "Parts Delivery Line Figure Token 6": MMXCMLocationData(
    name="Parts Delivery Line 6",
    code=192,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A216A, bit_position=2)
  ),
  "Parts Delivery Line Figure Token 7": MMXCMLocationData(
    name="Parts Delivery Line 7",
    code=193,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A216A, bit_position=3)
  ),
  "Parts Delivery Line Figure Token 8": MMXCMLocationData(
    name="Parts Delivery Line 8",
    code=194,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A216A, bit_position=4)
  ),
  "Computer Room Hunter Missile": MMXCMLocationData(
    name="Computer Room 1",
    code=195,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A216A, bit_position=6)
  ),
  "Computer Room Build Armor": MMXCMLocationData(
    name="Computer Room 2",
    code=196,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A216A, bit_position=7)
  ),
  "Computer Room Build Shield": MMXCMLocationData(
    name="Computer Room 3",
    code=197,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2169, bit_position=0)
  ),
  "Assembly Line Monitor Room Backup": MMXCMLocationData(
    name="Assembly Line Monitor Room 1",
    code=198,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2169, bit_position=1)
  ),
  "Assembly Line Monitor Room Build Power": MMXCMLocationData(
    name="Assembly Line Monitor Room 2",
    code=199,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2169, bit_position=2)
  ),
  "Computer Room Corridor Tank Energy 100 1": MMXCMLocationData(
    name="Computer Room Corridor 1",
    code=200,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2169, bit_position=3)
  ),
  "Computer Room Corridor Tank Energy 100 2": MMXCMLocationData(
    name="Computer Room Corridor 2",
    code=201,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2169, bit_position=4)
  ),
  "Computer Room Corridor Gain Hyper": MMXCMLocationData(
    name="Computer Room Corridor 3",
    code=202,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A2169, bit_position=5)
  ),
}
      
GIMIALLA_MINE_LOCATIONS: dict[str, MMXCMLocationData] = {
  "Level 1 Shaft Entrance Ultra Fire": MMXCMLocationData(
    name="Level 1 Shaft Entrance 1",
    code=203,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A2169, bit_position=7)
  ),
  "Level 1 Shaft Entrance Ultra Blizzard": MMXCMLocationData(
    name="Level 1 Shaft Entrance 2",
    code=204,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A2168, bit_position=0)
  ),
  "Level 1 Shaft Entrance Ultra Thunder": MMXCMLocationData(
    name="Level 1 Shaft Entrance 3",
    code=205,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A2168, bit_position=1)
  ),
  "Level 2 Main Tunnel Anti-Lock": MMXCMLocationData(
    name="Level 2 Main Tunnel 1",
    code=206,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A2168, bit_position=3)
  ),
  "Level 2 Main Tunnel DOA Protection": MMXCMLocationData(
    name="Level 2 Main Tunnel 2",
    code=207,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A2168, bit_position=4)
  ),
  "Level 2 Main Tunnel 1200z": MMXCMLocationData(
    name="Level 2 Main Tunnel 3",
    code=208,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A2168, bit_position=5)
  ),
  "Level 2 Main Tunnel Figure Token 1": MMXCMLocationData(
    name="Level 2 Main Tunnel 4",
    code=209,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A2168, bit_position=6)
  ),
  "Level 2 Main Tunnel Figure Token 2": MMXCMLocationData(
    name="Level 2 Main Tunnel 5",
    code=210,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A2168, bit_position=7)
  ),
  "L2 Northwest Division Figure Token 1": MMXCMLocationData(
    name="L2 Northwest Division 1",
    code=211,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216F, bit_position=0)
  ),
  "L2 Northwest Division Figure Token 2": MMXCMLocationData(
    name="L2 Northwest Division 2",
    code=212,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216F, bit_position=1)
  ),
  "L2 Northwest Division Figure Token 3": MMXCMLocationData(
    name="L2 Northwest Division 3",
    code=213,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216F, bit_position=2)
  ),
  "L2 Southwest Division Mini Motor": MMXCMLocationData(
    name="L2 Southwest Division 1",
    code=214,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216F, bit_position=7)
  ),
  # Note that this is using the flag for Booster Parts, not the Booster Parts themselves.
  "L2 Southwest Division Booster Parts": MMXCMLocationData(
    name="L2 Southwest Division Booster Parts 1",
    code=215,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A210E, bit_position=4)
  ),
  "L2 Southeast Division Ace of Spades": MMXCMLocationData(
    name="L2 Southeast Division 1",
    code=216,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216E, bit_position=1)
  ),
  "L2 Southeast Division Figure Token": MMXCMLocationData(
    name="L2 Southeast Division 2",
    code=217,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216E, bit_position=2)
  ),
  "L2 Northeast Division Tank Parts": MMXCMLocationData(
    name="L2 Northeast Division 1",
    code=218,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216F, bit_position=3)
  ),
  "L2 Northeast Division Build LE": MMXCMLocationData(
    name="L2 Northeast Division 2",
    code=219,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216F, bit_position=4)
  ),
  "L2 Northeast Division 800 FME": MMXCMLocationData(
    name="L2 Northeast Division 3",
    code=220,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216F, bit_position=5)
  ),
  "Level 3 Main Tunnel Figure Token 1": MMXCMLocationData(
    name="Level 3 Main Tunnel 1",
    code=221,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216E, bit_position=3)
  ),
  "Level 3 Main Tunnel Figure Token 2": MMXCMLocationData(
    name="Level 3 Main Tunnel 2",
    code=222,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216E, bit_position=4)
  ),
  "Level 3 Main Tunnel Tank Energy 100": MMXCMLocationData(
    name="Level 3 Main Tunnel 3",
    code=223,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216E, bit_position=5)
  ),
  "L3 Main Tunnel Blue Miner Trade Complete": MMXCMLocationData(
    name="Level 3 Main Tunnel Blue Miner 1",
    code=224,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A2113, bit_position=4)
  ),
  "L3 Northwest Division Ace of Hearts": MMXCMLocationData(
    name="L3 Northwest Division 1",
    code=225,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216D, bit_position=0)
  ),
  "L3 Northwest Division Figure Token": MMXCMLocationData(
    name="L3 Northwest Division 2",
    code=226,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216D, bit_position=1)
  ),
  "L3 Northwest Division 1300z": MMXCMLocationData(
    name="L3 Northwest Division 3",
    code=227,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216D, bit_position=2)
  ),
  "L3 Northwest Division Red Miner Trade Complete": MMXCMLocationData(
    name="L3 Northwest Division Red Miner 1",
    code=228,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A210D, bit_position=5)
  ),
  "L3 Northwest Division Yellow Miner Trade Complete": MMXCMLocationData(
    name="L3 Northwest Division Yellow Miner 1",
    code=229,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A210C, bit_position=2)
  ),
  "L3 Northeast Division Force Missiles": MMXCMLocationData(
    name="L3 Northeast Division 1",
    code=230,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216D, bit_position=3)
  ),
  "L3 Northeast Division Green Miner Trade Complete": MMXCMLocationData(
    name="L3 Northeast Division Green Miner 1",
    code=231,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A210C, bit_position=7) 
  ),
  "L3 Southwest Division Tank Parts": MMXCMLocationData(
    name="L3 Southwest Division 1",
    code=232,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216D, bit_position=5) 
  ),
  "L3 Southwest Division Figure Token 1": MMXCMLocationData(
    name="L3 Southwest Division 2",
    code=233,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216D, bit_position=6)
  ),
  "L3 Southwest Division Figure Token 2": MMXCMLocationData(
    name="L3 Southwest Division 3",
    code=234,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216D, bit_position=7)
  ),
  "Level 4 Main Tunnel Tank Energy 100": MMXCMLocationData(
    name="Level 4 Main Tunnel 1",
    code=235,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216C, bit_position=0)
  ),
  "Level 4 Main Tunnel Gain Hyper": MMXCMLocationData(
    name="Level 4 Main Tunnel 2",
    code=236,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216C, bit_position=1)
  ),
  "Level 4 Main Tunnel Build Power": MMXCMLocationData(
    name="Level 4 Main Tunnel 3",
    code=237,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216C, bit_position=2)
  ),
  "Level 4 Main Tunnel Build Armor": MMXCMLocationData(
    name="Level 4 Main Tunnel 4",
    code=238,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216C, bit_position=3)
  ),
  "Level 4 Main Tunnel Build Shield": MMXCMLocationData(
    name="Level 4 Main Tunnel 5",
    code=239,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216C, bit_position=4)
  ),
  "Level 4 Main Tunnel Build Speed": MMXCMLocationData(
    name="Level 4 Main Tunnel 6",
    code=240,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216C, bit_position=5)
  ),
  "Level 4 Main Tunnel Build WE": MMXCMLocationData(
    name="Level 4 Main Tunnel 7",
    code=241,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216C, bit_position=6)
  ),
  "Level 4 Durability Lab Fire Guard": MMXCMLocationData(
    name="Level 4 Durability Lab 1",
    code=242,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A216C, bit_position=7)
  ),
  "Level 4 Durability Lab Water Guard": MMXCMLocationData(
    name="Level 4 Durability Lab 2",
    code=243,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A2173, bit_position=0)
  ),
  "Level 4 Durability Lab Thunder Guard": MMXCMLocationData(
    name="Level 4 Durability Lab 3",
    code=244,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A2173, bit_position=1)
  ),     
}

VANALLIA_DESERT_LOCATIONS: dict[str, MMXCMLocationData] = {
  "Quicksand Figure Token 55%": MMXCMLocationData(
    name="Quicksand Item 1-1",
    code=245,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2148, bit_position=0)
  ),
  "Quicksand Figure Token Teleporter": MMXCMLocationData(
    name="Quicksand Item 1-2",
    code=246,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2148, bit_position=1)
  ),
  "Quicksand Figure Token 15%": MMXCMLocationData(
    name="Quicksand Item 1-3",
    code=247,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2148, bit_position=2)
  ),
  "Quicksand Mini Battery": MMXCMLocationData(
    name="Quicksand Item 1-4",
    code=248,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2149, bit_position=5)
  ),
  "Quicksand Tank Parts": MMXCMLocationData(
    name="Quicksand Item 1-5",
    code=249,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2149, bit_position=6)
  ),
  "Quicksand Doubletooth": MMXCMLocationData(
    name="Quicksand Item 1-6",
    code=250,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2149, bit_position=7)
  ),
  "Quicksand South Side Tank Energy 50": MMXCMLocationData(
    name="Quicksand South Side 1",
    code=251,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2172, bit_position=4)
  ),
  "Quicksand South Side Vaccine Program": MMXCMLocationData(
    name="Quicksand South Side 2",
    code=252,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2172, bit_position=5)
  ),
  "Quicksand South Side Cooler": MMXCMLocationData(
    name="Quicksand South Side 3",
    code=253,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2172, bit_position=6)
  ),
  "Quicksand South Side Build Power": MMXCMLocationData(
    name="Quicksand South Side 4",
    code=254,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2172, bit_position=7)
  ),
  "Quicksand South Side Build Armor": MMXCMLocationData(
    name="Quicksand South Side 5",
    code=255,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2171, bit_position=0)
  ),
  "Quicksand South Side Build Shield": MMXCMLocationData(
    name="Quicksand South Side 6",
    code=256,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2171, bit_position=1)
  ),
  "Quicksand South Side Build Speed": MMXCMLocationData(
    name="Quicksand South Side 7",
    code=257,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2171, bit_position=2)
  ),
  "Quicksand North Side Cure All": MMXCMLocationData(
    name="Quicksand North Side 1",
    code=258,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2171, bit_position=6)
  ),
  "Quicksand North Side 1800z": MMXCMLocationData(
    name="Quicksand North Side 2",
    code=259,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2171, bit_position=7)
  ),
  "Quicksand North Side 2000z": MMXCMLocationData(
    name="Quicksand North Side 3",
    code=260,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2170, bit_position=0)
  ),
  "Quicksand North Side 400FME 1": MMXCMLocationData(
    name="Quicksand North Side 4",
    code=261,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2170, bit_position=1)
  ),
  "Quicksand North Side 400FME 2": MMXCMLocationData(
    name="Quicksand North Side 5",
    code=262,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2170, bit_position=2)
  ),
  "Quicksand North Side Build Hyper": MMXCMLocationData(
    name="Quicksand North Side 6",
    code=263,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2170, bit_position=3)
  ),
  "Quicksand North Side Ball & Chain Hammer": MMXCMLocationData(
    name="Quicksand North Side Ball & Chain Hammer 1",
    code=264,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2186, bit_position=2)
  ),
  "Quicksand Central Passageway Tank Energy 100": MMXCMLocationData(
    name="Quicksand Central Passageway 1",
    code=265,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2170, bit_position=6)
  ),
  "Quicksand Central Passageway Gain Hyper": MMXCMLocationData(
    name="Quicksand Central Passageway 2",
    code=266,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2170, bit_position=7)
  ),
  "Signal Jammer Laser Energy Control Room SW Tank Energy 50": MMXCMLocationData(
    name="Signal Jammer Laser Energy Control Room SW 1",
    code=267,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2177, bit_position=5)
  ),
  "Signal Jammer Laser Energy Control Room NW Figure Token 1": MMXCMLocationData(
    name="Signal Jammer Laser Energy Control Room NW 1",
    code=268,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2177, bit_position=1)
  ),
  "Signal Jammer Laser Energy Control Room NW Figure Token 2": MMXCMLocationData(
    name="Signal Jammer Laser Energy Control Room NW 2",
    code=269,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2177, bit_position=2)
  ),
  "Signal Jammer Laser Energy Control Room NE Figure Token 1": MMXCMLocationData(
    name="Signal Jammer Laser Energy Control Room NE 1",
    code=270,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2177, bit_position=3)
  ),
  "Signal Jammer Laser Energy Control Room NE Figure Token 2": MMXCMLocationData(
    name="Signal Jammer Laser Energy Control Room NE 2",
    code=271,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2177, bit_position=4)
  ),
  "Signal Jammer Laser Energy Control Room SE Cyber Liquid": MMXCMLocationData(
    name="Signal Jammer Laser Energy Control Room SE 1",
    code=272,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2177, bit_position=0)
  ),
  "Signal Jammer Laser Energy Generator Figure Token 1": MMXCMLocationData(
    name="Signal Jammer Laser Energy Generator 1",
    code=273,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2175, bit_position=0)
  ),
  "Signal Jammer Laser Energy Generator Fire Resist": MMXCMLocationData(
    name="Signal Jammer Laser Energy Generator 2",
    code=274,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2175, bit_position=1)
  ),
  "Signal Jammer Laser Energy Generator Thunder Stella": MMXCMLocationData(
    name="Signal Jammer Laser Energy Generator 3",
    code=275,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2176, bit_position=0)
  ),
  "Signal Jammer Laser Energy Generator Build LE": MMXCMLocationData(
    name="Signal Jammer Laser Energy Generator 4",
    code=276,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2176, bit_position=1)
  ),
  "Signal Jammer Laser Energy Generator Build WE": MMXCMLocationData(
    name="Signal Jammer Laser Energy Generator 5",
    code=277,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2176, bit_position=2)
  ),
  "Signal Jammer Laser Energy Generator Combat Absorber": MMXCMLocationData(
    name="Signal Jammer Laser Energy Generator 6",
    code=278,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2176, bit_position=3)
  ),
  "Signal Jammer Laser Energy Generator Shot Absorber": MMXCMLocationData(
    name="Signal Jammer Laser Energy Generator 7",
    code=279,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2176, bit_position=4)
  ),
  "Signal Jammer Laser Energy Generator Figure Token 2": MMXCMLocationData(
    name="Signal Jammer Laser Energy Generator 8",
    code=280,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2176, bit_position=5)
  ),
  "Signal Jammer Laser Energy Generator Figure Token 3": MMXCMLocationData(
    name="Signal Jammer Laser Energy Generator 9",
    code=281,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2176, bit_position=6)
  ),
  "Signal Jammer Laser Energy Generator Figure Token 4": MMXCMLocationData(
    name="Signal Jammer Laser Energy Generator 10",
    code=282,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A2176, bit_position=7)
  ),        
}

MELDA_ORE_PLANT_LOCATIONS: dict[str, MMXCMLocationData] = {
  "Ore Plant External Tank MD 1": MMXCMLocationData(
    name="Ore Plant External Tank 1",
    code=283,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2175, bit_position=2)
  ),
  "Ore Plant External Tank MD 2": MMXCMLocationData(
    name="Ore Plant External Tank 2",
    code=284,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2175, bit_position=3)
  ),
  "Ore Plant External Tank MD 3": MMXCMLocationData(
    name="Ore Plant External Tank 3",
    code=285,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2175, bit_position=4)
  ),
  "Ore Plant External Tank MD 4": MMXCMLocationData(
    name="Ore Plant External Tank 4",
    code=286,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2175, bit_position=5)
  ),
  "B1 Entrance Hall MD 1": MMXCMLocationData(
    name="B1 Entrance Hall 1",
    code=287,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2174, bit_position=1)
  ),
  "B1 Entrance Hall MD 2": MMXCMLocationData(
    name="B1 Entrance Hall 2",
    code=288,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2174, bit_position=0)
  ),
  "B1 Entrance Hall MD 3": MMXCMLocationData(
    name="B1 Entrance Hall 3",
    code=289,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2175, bit_position=6)
  ),
  "B1 Entrance Hall MD 4": MMXCMLocationData(
    name="B1 Entrance Hall 4",
    code=290,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2175, bit_position=7)
  ),
  "Area E-B02 MD 1": MMXCMLocationData(
    name="Area E-B02-1",
    code=291,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A217B, bit_position=1)
  ),
  "Area E-B02 MD 2": MMXCMLocationData(
    name="Area E-B02-2",
    code=292,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A217B, bit_position=2)
  ),
  "Area E-B02 MD 3": MMXCMLocationData(
    name="Area E-B02-3",
    code=293,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A217B, bit_position=3)
  ),
  "Area E-B03 MD 1": MMXCMLocationData(
    name="Area E-B03-1",
    code=294,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A217A, bit_position=1)
  ),
  "Area E-B03 MD 2": MMXCMLocationData(
    name="Area E-B03-2",
    code=295,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A217A, bit_position=2)
  ),
  "Area E-B03 MD 3": MMXCMLocationData(
    name="Area E-B03-3",
    code=296,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A217A, bit_position=3)
  ),
  "Area E-B04 MD 1": MMXCMLocationData(
    name="Area E-B04-1",
    code=297,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2179, bit_position=0)
  ),
  "Area E-B04 MD 2": MMXCMLocationData(
    name="Area E-B04-2",
    code=298,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2179, bit_position=1)
  ),
  "Missile Silo Base Lower Section MD 1": MMXCMLocationData(
    name="Missile Silo Base Lower Section 1",
    code=299,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2179, bit_position=3)
  ),
  "Missile Silo Base Lower Section MD 2": MMXCMLocationData(
    name="Missile Silo Base Lower Section 2",
    code=300,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2179, bit_position=4)
  ),
  "Missile Silo Base Lower Section MD 3": MMXCMLocationData(
    name="Missile Silo Base Lower Section 3",
    code=301,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2179, bit_position=5)
  ),
  "Missile Silo Base Lower Section MD 4": MMXCMLocationData(
    name="Missile Silo Base Lower Section 4",
    code=302,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2179, bit_position=6)
  ),
  "B5 - East-West Block Access Tunnel MD 1": MMXCMLocationData(
    name="B5 - East-West Block Access Tunnel 1",
    code=303,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2179, bit_position=2)
  ),
  "Area W-B03 MD 1": MMXCMLocationData(
    name="Area W-B03 1",
    code=304,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A217B, bit_position=5)
  ),
  "Area W-B03 MD 2": MMXCMLocationData(
    name="Area W-B03 2",
    code=305,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A21BA, bit_position=6)
  ),
  "Area W-B03 MD 3": MMXCMLocationData(
    name="Area W-B03 3",
    code=306,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A217B, bit_position=7)
  ),
  "Area W-B02 MD 1": MMXCMLocationData(
    name="Area W-B02 1",
    code=307,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2174, bit_position=5)
  ),
  "Area W-B02 MD 2": MMXCMLocationData(
    name="Area W-B02 2",
    code=308,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2174, bit_position=6)
  ),
  "Area W-B02 MD 3": MMXCMLocationData(
    name="Area W-B02 3",
    code=309,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2174, bit_position=7)
  ),
  "Missile Warhead Adjustment Room MD 1": MMXCMLocationData(
    name="Missile Warhead Adjustment Room 1",
    code=310,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2179, bit_position=7)
  ),
  "Area W-B01 MD 1": MMXCMLocationData(
    name="Area W-B01-1",
    code=311,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2174, bit_position=3)
  ),
  "Missile Maintenance Room MD 1": MMXCMLocationData(
    name="Missile Maintenance Room 1",
    code=312,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A2178, bit_position=0)
  ),
}

GRAVE_RUINS_BASE_LOCATIONS: dict[str, MMXCMLocationData] = {
  "Level E Security Zone MD 1": MMXCMLocationData(
    name="Level E Security Zone 1",
    code=313,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A2178, bit_position=2)
  ),
  "Level E Security Zone MD 2": MMXCMLocationData(
    name="Level E Security Zone 2",
    code=314,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A2178, bit_position=3)
  ),
  "Level D Security Zone MD 1": MMXCMLocationData(
    name="Level D Security Zone 1",
    code=315,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A2178, bit_position=5)
  ),
  "Level C Security Zone MD 1": MMXCMLocationData(
    name="Level C Security Zone 1",
    code=316,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A2178, bit_position=7)
  ),
  "Level C Security Zone MD 2": MMXCMLocationData(
    name="Level C Security Zone 2",
    code=317,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217F, bit_position=0)
  ),
  "Level C Security Zone MD 3": MMXCMLocationData(
    name="Level C Security Zone 3",
    code=318,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217F, bit_position=1)
  ),
  "Level C Security Zone MD 4": MMXCMLocationData(
    name="Level C Security Zone 4",
    code=319,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217F, bit_position=2)
  ),
  "Level C Security Zone MD 5": MMXCMLocationData(
    name="Level C Security Zone 5",
    code=320,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217F, bit_position=3)
  ),
  "Level B Security Zone MD 1": MMXCMLocationData(
    name="Level B Security Zone 1",
    code=321,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217F, bit_position=7)
  ),
  "Level B Security Zone MD 2": MMXCMLocationData(
    name="Level B Security Zone 2",
    code=322,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217E, bit_position=0)
  ),
  "Battle Field MD 1": MMXCMLocationData(
    name="Battle Field 1",
    code=323,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A2183, bit_position=0)
  ),
  "Battle Field MD 2": MMXCMLocationData(
    name="Battle Field 2",
    code=324,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A2183, bit_position=1)
  ),
  "Battle Field MD 3": MMXCMLocationData(
    name="Battle Field 3",
    code=325,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A2183, bit_position=2)
  ),
  "Battle Field MD 4": MMXCMLocationData(
    name="Battle Field 4",
    code=326,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A2183, bit_position=3)
  ),
  "Battle Field MD 5": MMXCMLocationData(
    name="Battle Field 5",
    code=327,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217C, bit_position=5)
  ),
  "Battle Field MD 6": MMXCMLocationData(
    name="Battle Field 6",
    code=328,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217C, bit_position=6)
  ),
  "Battle Field MD 7": MMXCMLocationData(
    name="Battle Field 7",
    code=329,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217C, bit_position=7)
  ),
  "Revolver Shaft Area MD 1": MMXCMLocationData(
    name="Revolver Shaft Area 1",
    code=330,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217E, bit_position=2)
  ),
  "Revolver Shaft Area MD 2": MMXCMLocationData(
    name="Revolver Shaft Area 2",
    code=331,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217E, bit_position=3)
  ),
  "Revolver Room #4 MD 1": MMXCMLocationData(
    name="Revolver Room #4 1",
    code=332,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217E, bit_position=5)
  ),
  "Revolver Room #6 MD 1": MMXCMLocationData(
    name="Revolver Room #6 1",
    code=333,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217E, bit_position=6)
  ),
  "Revolver Room #7 MD 1": MMXCMLocationData(
    name="Revolver Room #7 1",
    code=334,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217E, bit_position=7)
  ),
  "Revolver Shaft Area Right Side MD 1": MMXCMLocationData(
    name="Revolver Shaft Area Right Side 1",
    code=335,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217E, bit_position=4)
  ),
  "Level S Top Security Zone MD 1": MMXCMLocationData(
    name="Level S Top Security Zone 1",
    code=336,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217D, bit_position=1)
  ),
  "Level S Top Security Zone MD 2": MMXCMLocationData(
    name="Level S Top Security Zone 2",
    code=337,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217D, bit_position=2)
  ),
  "Level S Top Security Zone MD 3": MMXCMLocationData(
    name="Level S Top Security Zone 3",
    code=338,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217D, bit_position=3)
  ),
  "Level S Top Security Zone MD 4": MMXCMLocationData(
    name="Level S Top Security Zone 4",
    code=339,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217D, bit_position=4)
  ),
  "Level S Top Security Zone MD 5": MMXCMLocationData(
    name="Level S Top Security Zone 5",
    code=340,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217C, bit_position=0)
  ),
  "Level S Top Security Zone MD 6": MMXCMLocationData(
    name="Level S Top Security Zone 6",
    code=341,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217C, bit_position=1)
  ),
  "Level S Top Security Zone MD 7": MMXCMLocationData(
    name="Level S Top Security Zone 7",
    code=342,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217D, bit_position=5)
  ),
  "Level S Top Security Zone MD 8": MMXCMLocationData(
    name="Level S Top Security Zone 8",
    code=343,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217D, bit_position=6)
  ),
  "Level S Top Security Zone MD 9": MMXCMLocationData(
    name="Level S Top Security Zone 9",
    code=344,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217D, bit_position=7)
  ),
  "Final Gate MD 1": MMXCMLocationData(
    name="Final Gate 1",
    code=345,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217C, bit_position=2)
  ),
  "Final Gate MD 2": MMXCMLocationData(
    name="Final Gate 2",
    code=346,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217C, bit_position=3)
  ),
  "Final Gate MD 3": MMXCMLocationData(
    name="Final Gate 3",
    code=347,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A217C, bit_position=4)
  ),
}

FAR_EAST_HQ_LOCATIONS: dict[str, MMXCMLocationData] = {
  "Teleport Terminal MD 1": MMXCMLocationData(
    name="Teleport Terminal 1",
    code=348,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2181, bit_position=0)
  ),
  "Teleport Terminal MD 2": MMXCMLocationData(
    name="Teleport Terminal 2",
    code=349,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2181, bit_position=1)
  ),
  "Teleport Terminal MD 3": MMXCMLocationData(
    name="Teleport Terminal 3",
    code=350,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2182, bit_position=6)
  ),
  "Teleport Terminal MD 4": MMXCMLocationData(
    name="Teleport Terminal 4",
    code=351,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2182, bit_position=7)
  ),
  "Final Gate Chapter 10 MD 1": MMXCMLocationData(
    name="Final Gate Chapter 10-1",
    code=352,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2183, bit_position=4)
  ),
  "Final Gate Chapter 10 MD 2": MMXCMLocationData(
    name="Final Gate Chapter 10-2",
    code=353,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2183, bit_position=5)
  ),
  "Final Gate Chapter 10 MD 3": MMXCMLocationData(
    name="Final Gate Chapter 10-3",
    code=354,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2183, bit_position=6)
  ),
  "Final Gate Chapter 10 MD 4": MMXCMLocationData(
    name="Final Gate Chapter 10-4",
    code=355,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2183, bit_position=7)
  ),
  "Final Gate Chapter 10 MD 5": MMXCMLocationData(
    name="Final Gate Chapter 10-5",
    code=356,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2182, bit_position=0)
  ),
  "Final Gate Chapter 10 MD 6": MMXCMLocationData(
    name="Final Gate Chapter 10-6",
    code=357,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2182, bit_position=1)
  ),
  "Final Gate Chapter 10 MD 7": MMXCMLocationData(
    name="Final Gate Chapter 10-7",
    code=358,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2182, bit_position=2)
  ),
  "Final Gate Chapter 10 MD 8": MMXCMLocationData(
    name="Final Gate Chapter 10-8",
    code=359,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2182, bit_position=3)
  ),
  "Super-Strato Terminal MD 1": MMXCMLocationData(
    name="Super Strato Terminal 1",
    code=360,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2181, bit_position=2)
  ),
  "Blue Earth Tunnel MD 1": MMXCMLocationData(
    name="Blue Earth Tunnel 1",
    code=361,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2182, bit_position=4)
  ),
  "Blue Earth Tunnel MD 2": MMXCMLocationData(
    name="Blue Earth Tunnel 2",
    code=362,
    parent_region="Far East HQ",
    ram_addr=MMXCMRamData(0x804A2182, bit_position=5)
  ),
  #  Sets the MMXCMLocationData for the final boss! (Great Redips)
  "Defeated Great Redips": MMXCMLocationData(
    name="Defeated Great Redips",
    code=None,
    parent_region="Far East HQ",
    event_item=True,
    ram_addr=MMXCMRamData(ram_addr=0x804A210A, bit_position=3)
  ),
}

MECHANILOIDS_LOCATIONS: dict[str, MMXCMLocationData] = {
  "Deerball": MMXCMLocationData(
    name="Deerball",
    code=363,
    parent_region="Lagrano Ruins",
    ram_addr=MMXCMRamData(0x804A212D, bit_position=5)
  ),                                                                                  
  "Radar Killer": MMXCMLocationData(
    name="Radar Killer",
    code=364,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A212E, bit_position=3)
  ),
  "Blowfish": MMXCMLocationData(
    name="Blowfish",
    code=365,
    parent_region="Tianna Camp",
    ram_addr=MMXCMRamData(0x804A212C, bit_position=1)
  ),
  "Big Monkey": MMXCMLocationData(
    name="Big Monkey",
    code=366,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A212E, bit_position=0)
  ),
  "Preon": MMXCMLocationData(
    name="Preon",
    code=367,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A212D, bit_position=0)
  ),
  "Dober Man": MMXCMLocationData(
    name="Dober Man",
    code=368,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A212D, bit_position=1)
  ),
  "Mettaur": MMXCMLocationData(
    name="Mettaur",
    code=369,
    parent_region="Gaudile Laboratory",
    ram_addr=MMXCMRamData(0x804A212C, bit_position=2)
  ),
  "Einhammer": MMXCMLocationData(
    name="Einhammer",
    code=370,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A212E, bit_position=1)
  ),
  "Killer Mantis": MMXCMLocationData(
    name="Killer Mantis",
    code=371,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A212E, bit_position=2)
  ),
  "Rush Loader": MMXCMLocationData(
    name="Rush Loader",
    code=372,
    parent_region="Ulfat Factory",
    ram_addr=MMXCMRamData(0x804A212D, bit_position=2)
  ),
  "Mega Mantor": MMXCMLocationData(
    name="Mega Mantor",
    code=373,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A212E, bit_position=4)
  ),
  "Degraver": MMXCMLocationData(
    name="Degraver",
    code=374,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A212D, bit_position=3)
  ),
  "Bat Bone": MMXCMLocationData(
    name="Bat Bone",
    code=375,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A212C, bit_position=0)
  ),
  "Gold Blader": MMXCMLocationData(
    name="Gold Blader",
    code=376,
    parent_region="Gimialla Mine",
    ram_addr=MMXCMRamData(0x804A212C, bit_position=5)
  ),
  "Liquid Glob": MMXCMLocationData(
    name="Liquid Glob",
    code=377,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A212E, bit_position=5)
  ),
  "Mega Tortoise": MMXCMLocationData(
    name="Mega Tortoise",
    code=378,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A212D, bit_position=4)
  ),
  "Pararoid": MMXCMLocationData(
    name="Pararoid",
    code=379,
    parent_region="Vanallia Desert",
    ram_addr=MMXCMRamData(0x804A212C, bit_position=3)
  ),
  "Meltdown": MMXCMLocationData(
    name="Meltdown", 
    code=380,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A212E, bit_position=6)
  ),
  "Rabbid": MMXCMLocationData(
    name="Rabbid",
    code=381,
    parent_region="Melda Ore Plant",
    ram_addr=MMXCMRamData(0x804A212C, bit_position=4)
  ),
  "Bladey": MMXCMLocationData(
    name="Bladey",
    code=382,
    parent_region="Grave Ruins Base",
    ram_addr=MMXCMRamData(0x804A212C, bit_position=6)
  ),
}

"""CHAPTER_CLEAR_LOCATIONS: dict[str, MMXCMLocationData] = {
    "Lagrano Ruins Clear": {
        "ram_addr": MMXCMLocationData(ram_addr=0xCAFE00D0, bit_position=0), # Placeholder RAM Address - REPLACE LATER
        "item_id": items.ALL_ITEMS_TABLE["Rebellion Medal (Lagrano Ruins)"]["item_id"]
    },
    "Central Tower Clear": {
        "ram_addr": MMXCMLocationData(ram_addr=0xCAFE00D1, bit_position=0), # Placeholder RAM Address - REPLACE LATER
        "item_id": items.ALL_ITEMS_TABLE["Rebellion Medal (Central Tower)"]["item_id"]
    },
    "Tianna Camp Clear": {
        "ram_addr": MMXCMLocationData(ram_addr=0xCAFE00D2, bit_position=0), # Placeholder RAM Address - REPLACE LATER
        "item_id": items.ALL_ITEMS_TABLE["Rebellion Medal (Tianna Camp)"]["item_id"]
    },
    "Gaudile Laboratory Clear": {
        "ram_addr": MMXCMLocationData(ram_addr=0xCAFE00D3, bit_position=0), # Placeholder RAM Address - REPLACE LGCAL
        "item_id": items.ALL_ITEMS_TABLE["Rebellion Medal (Gaudile Laboratory)"]["item_id"]
    },
    "Ulfat Factory Clear": {
        "ram_addr": MMXCMLocationData(ram_addr=0xCAFE00D4, bit_position=0), # Placeholder RAM Address - REPLACE LATER
        "item_id": items.ALL_ITEMS_TABLE["Rebellion Medal (Ulfat Factory)"]["item_id"]
    },
    "Gimialla Mine Clear": {
        "ram_addr": MMXCMLocationData(ram_addr=0xCAFE00D5, bit_position=0), # Placeholder RAM Address - REPLACE LATER
        "item_id": items.ALL_ITEMS_TABLE["Rebellion Medal (Gimialla Mine)"]["item_id"]
    },
    "Vanallia Desert Clear": {
        "ram_addr": MMXCMLocationData(ram_addr=0xCAFE00D6, bit_position=0), # Placeholder RAM Address - REPLACE LATER
        "item_id": items.ALL_ITEMS_TABLE["Rebellion Medal (Vanallia Desert)"]["item_id"]
    },
    "Melda Ore Plant Clear": {
        "ram_addr": MMXCMLocationData(ram_addr=0xCAFE00D7, bit_position=0), # Placeholder RAM Address - REPLACE LATER
        "item_id": items.ALL_ITEMS_TABLE["Rebellion Medal (Melda Ore Plant)"]["item_id"]
    },
    "Grave Ruins Base Clear": {
        "ram_addr": MMXCMRamData(ram_addr=0xCAFE00D8, bit_position=0), # Placeholder RAM Address - REPLACE LATER
        "item_id": items.ALL_ITEMS_TABLE["Rebellion Medal (Grave Ruins Base)"]["item_id"]
    },
}"""

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
  #**CHAPTER_CLEAR_LOCATIONS,
  **BOSS_DROPS_LOCATIONS,
  **SKY_ROOM_LOCATIONS,
}

# A Dictionary for looking up a location by its name!
LOCATION_LOOKUP_TABLE: dict[str, MMXCMLocationData] = {
  location.name: location for location in LOCATION_TABLE.values()
}
    
