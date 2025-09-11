from typing import NamedTuple, Dict, Optional, Set

from BaseClasses import Item
from BaseClasses import ItemClassification as IC 

# This will import from the Helpers.py in the same folder. 
from .Helpers import MMXCMRamData

# This will start our 'blueprint' for Mega Man X Command Mission items! 
class MMXCMItemData(NamedTuple):
  name: Optional[str] = None
  type: str
  code: Optional[int]
  classification: IC
  item_id: Optional[int] = None #This is the item's unique ID
  update_ram_addr: Optional[list[MMXCMRamData]] = None 

# This is the list for every single item we are currently randomzing in AP.
PROGRESSION_ITEM_TABLE: dict[str, MMXCMItemData] = {
  # Follow this example for every additional item. 
  "Aile ID": MMXCMItemData(
    type="Key Item",
    code=1,
    classification=IC.progression,
    # Note: since these addresses are the same RAM, we use bit_positions!
    update_ram_addr=[MMXCMRamData(0x804A2180, bit_position=3)]
  ),
  "Security Card": MMXCMItemData(
    type="Key Item", 
    code=2,
    classification=IC.progression,
    update_ram_addr=[MMXCMRamData(0x804A2180, bit_position=4)]
  ),
  "Prison ID": MMXCMItemData(
    type="Key Item",
    code=3,
    classification=IC.progression,
    update_ram_addr=[MMXCMRamData(0x804A2180, bit_position=5)]
  ),
  "Electric Components": MMXCMItemData(
    type="Key Item",
    code=4,
    classification=IC.progression,
    update_ram_addr=[MMXCMRamData(0x804A2185, bit_position=0)]
  ),
  "Booster Parts": MMXCMItemData( 
    type="Key Item",
    code=5,
    classification=IC.progression,
    update_ram_addr=[MMXCMRamData(0x804A2185, bit_position=7)]
  ),
  "Lagrano Ruins Access Code": MMXCMItemData(
    type="Key Item", 
    code=6,
    classification=IC.progression,
    update_ram_addr=None
  ),
  "Central Tower Access Code": MMXCMItemData(
    type="Key Item",
    code=7,
    classification=IC.progression,
    # Note: There are 3 changes here for the cutscenes, and Aile's Room.
    update_ram_addr=[
      MMXCMRamData(0x804A20BD, bit_position=6),
      MMXCMRamData(0x804A20BD, bit_position=7),
      MMXCMRamData(0x804A20C1, bit_position=0)
    ]
  ),
  "Tianna Camp Access Code": MMXCMItemData(
    type="Key Item",
    code=8,
    classification=IC.progression,
    update_ram_addr=None
  ),
  "Gaudile Laboratory Access Code": MMXCMItemData(
    type="Key Item",
    code=9,
    classification=IC.progression,
    update_ram_addr=None
  ),
  "Ulfat Factory Access Code": MMXCMItemData(
    type="Key Item",
    code=10,
    classification=IC.progression,
    update_ram_addr=None
  ),
  "Gimialla Mine Access Code": MMXCMItemData(
    type="Key Item",
    code=11,
    classification=IC.progression,
    update_ram_addr=None
  ),
  "Vanallia Desert Access Code": MMXCMItemData(
    type="Key Item",
    code=12,
    classification=IC.progression,
    update_ram_addr=None
  ),
  "Melda Ore Plant Access Code": MMXCMItemData(
    type="Key Item",
    code=13,
    classification=IC.progression,
    update_ram_addr=None
  ),
  "Grave Ruins Base Access Code": MMXCMItemData(
    type="Key Item",
    code=14,
    classification=IC.progression,
    update_ram_addr=None
  ),
  "Far East HQ Access Code": MMXCMItemData(
    type="Key Item",
    code=15,
    classification=IC.progression,
    update_ram_addr=[
      MMXCMRamData(0x804A2128, bit_position=0),
      MMXCMRamData(0x804A2128, bit_position=1)
    ]
  )
}

USEFUL_ITEM_TABLE: dict[str, MMXCMItemData] = {
  # This is the list of Useful items, like armors and keys.
  "Treasure Radar": MMXCMItemData(
    type="Major Item",
    code=16,
    classification=IC.useful,
    update_ram_addr=[MMXCMRamData(0x804A2187, bit_position=1)]
  ),
  "Lagrano Key": MMXCMItemData(
    type="Major Item",
    code=17,
    classification=IC.useful,
    update_ram_addr=[MMXCMRamData(0x804A2187, bit_position=2)]
  ),
  "Tianna Key": MMXCMItemData(
    type="Major Item",
    code=18,
    classification=IC.useful,
    update_ram_addr=[MMXCMRamData(0x804A2187, bit_position=3)]
  ),
  "Gimialla Key": MMXCMItemData(
    type="Major Item",
    code=19,
    classification=IC.useful,
    update_ram_addr=[MMXCMRamData(0x804A2187, bit_position=4)]
  ),
  "Melda Key": MMXCMItemData(
    type="Major Item",
    code=20,
    classification=IC.useful,
    update_ram_addr=[MMXCMRamData(0x804A2187, bit_position=5)]
  ),
  "Central Key": MMXCMItemData(
    type="Major Item",
    code=21,
    classification=IC.useful,
    update_ram_addr=[MMXCMRamData(0x804A2187, bit_position=6)]
  ),
  "Ultimate Armor": MMXCMItemData(
    type="Major Item",
    code=22,
    classification=IC.useful,
    update_ram_addr=[MMXCMRamData(0x804A2180, bit_position=6)]
  ),
  "Absolute Armor": MMXCMItemData(
    type="Major Item",
    code=23,
    classification=IC.useful,
    update_ram_addr=[MMXCMRamData(0x804A2180, bit_position=7)]
  ),
  "Build LE": MMXCMItemData(
    type="Consumable",
    code=24,
    classification=IC.useful,
    item_id=15,
    update_ram_addr=None
  ),
  "Build Power": MMXCMItemData(
    type="Consumable",
    code=25,
    classification=IC.useful,
    item_id=16,
    update_ram_addr=None
  ),
  "Build Armor": MMXCMItemData(
    type="Consumable",
    code=26,
    classification=IC.useful,
    item_id=17,
    update_ram_addr=None
  ),
  "Build Shield": MMXCMItemData(
    type="Consumable",
    code=27,
    classification=IC.useful,
    item_id=18,
    update_ram_addr=None
  ),
  "Build Speed": MMXCMItemData(
    type="Consumable",
    code=28,
    classification=IC.useful,
    item_id=19,
    update_ram_addr=None
  ),
  "Build WE": MMXCMItemData(
    type="Consumable",
    code=29,
    classification=IC.useful,
    item_id=28,
    update_ram_addr=None
  ),
  "Build Hyper": MMXCMItemData(
    type="Consumable",
    code=30,
    classification=IC.useful,
    item_id=30,
    update_ram_addr=None
}

SUB_WEAPONS_TABLE: dict[str, MMXCMItemData] = {}
FORCE_METAL_TABLE: dict[str, MMXCMItemData] = {}

#Note for these: they will be DYNAMICALLY Stored in inventory via Patcher.py
FILLER_TABLE: dict[str, MMXCMItemData] = {
  "Vaccine Program": MMXCMItemData(
    type="Consumable",
    code=31,
    classification=IC.filler,
    item_id=1,
    update_ram_addr=None
  ),
  "Anti-Lock": MMXCMItemData(
    type="Consumable",
    code=32,
    classification=IC.filler,
    item_id=2,
    update_ram_addr=None
  ),
  "Warm-up": MMXCMItemData(
    type="Consumable",
    code=33,
    classification=IC.filler,
    item_id=3,
    update_ram_addr=None
  ),
  "Cooler": MMXCMItemData(
    type="Consumable",
    code=34,
    classification=IC.filler,
    item_id=4,
    update_ram_addr=None
  ),
  "Clear Vision": MMXCMItemData(
    type="Consumable",
    code=35,
    classification=IC.filler,
    item_id=5,
    update_ram_addr=None
  ),
  "Cure One": MMXCMItemData(
    type="Consumable",
    code=36,
    classification=IC.filler,
    item_id=6,
    update_ram_addr=None
  ),
  "Cure All": MMXCMItemData(
    type="Consumable",
    code=37,
    classification=IC.filler,
    item_id=7,
    update_ram_addr=None
  ),
  "Reboot": MMXCMItemData(
    type="Consumable",
    code=38,
    classification=IC.filler,
    item_id=8,
    update_ram_addr=None
  ),
  "Backup": MMXCMItemData(
    type="Consumable",
    code=39,
    classification=IC.filler,
    item_id=9,
    update_ram_addr=None
  ),
  "Boost Power": MMXCMItemData(
    type="Consumable",
    code=40,
    classification=IC.filler,
    item_id=10,
    update_ram_addr=None
  ),
  "Boost Armor": MMXCMItemData(
    type="Consumable",
    code=41,
    classification=IC.filler,
    item_id=11,
    update_ram_addr=None
  ),
  "Boost Shield": MMXCMItemData(
    type="Consumable",
    code=42,
    classification=IC.filler,
    item_id=12,
    update_ram_addr=None
  ),
  "Boost Speed": MMXCMItemData(
    type="Consumable",
    code=43,
    classification=IC.filler,
    item_id=13,
    update_ram_addr=None
  ),
  "Unlock Limiter": MMXCMItemData(
    type="Consumable",
    code=44,
    classification=IC.filler,
    item_id=14,
    update_ram_addr=None
  ),
  "Mega Fire": MMXCMItemData(
    type="Consumable",
    code=45,
    classification=IC.filler,
    item_id=20,
    update_ram_addr=None
  ),
  "Ultra Fire": MMXCMItemData(
    type="Consumable",
    code=46,
    classification=IC.filler,
    item_id=21,
    update_ram_addr=None
  ),
  "Mega Blizzard": MMXCMItemData(
    type="Consumable",
    code=47,
    classification=IC.filler,
    item_id=22,
    update_ram_addr=None
  ),
  "Ultra Blizzard": MMXCMItemData(
    type="Consumable",
    code=48,
    classification=IC.filler,
    item_id=23,
    update_ram_addr=None
  ),
  "Mega Thunder": MMXCMItemData(
    type="Consumable",
    code=49,
    classification=IC.filler,
    item_id=24,
    update_ram_addr=None
  ),
  "Ultra Thunder": MMXCMItemData(
    type="Consumable",
    code=50,
    classification=IC.filler,
    item_id=25,
    update_ram_addr=None
  ),
  "Liquid Suffocation": MMXCMItemData(
    type="Consumable",
    code=51,
    classification=IC.filler,
    item_id=26,
    update_ram_addr=None
  ),
  "Chaff": MMXCMItemData(
    type="Consumable",
    code=52,
    classification=IC.filler,
    item_id=27,
    update_ram_addr=None
  ),
  "Gain Hyper": MMXCMItemData(
    type="Consumable",
    code=53,
    classification=IC.filler,
    item_id=31,
    update_ram_addr=None
  
}

#Add any other tables here, Filler, Trap, etc.
WEAPONS_TABLE: dict[str, MMXCMItemData] = {
  # X's Non-progressive weapons:
  "Brave Buster": MMXCMItemData(
    type="Weapon",
    code=54,
    classification=IC.useful,
    item_id=48,
    update_ram_addr=None
  ),
  "Turbo Buster": MMXCMItemData(
    type="Weapon",
    code=55,
    classification=IC.useful,
    item_id=49,
    update_ram_addr=None
  ),
  # Zero's Non-Progressive Weapons:
  "Red Lotus Saber": MMXCMItemData(
    type="Weapon",
    code=56,
    classification=IC.useful,
    item_id=67,
    update_ram_addr=None
  ),
  "Soul Saber": MMXCMItemData(
    type="Weapon",
    code=57,
    classification=IC.useful,
    item_id=59,
    update_ram_addr=None
  ),
  # Spider's Non-Progressive Weapons:
  "Joker": MMXCMItemData(
    type="Weapon",
    code=58,
    classification=IC.useful,
    item_id=91,
    update_ram_addr=None
  ),
  # Massimo's Non-Progressive Weapons:
  "Interceptor": MMXCMItemData(
    type="Weapon",
    code=59,
    classification=IC.useful,
    item_id=110,
    update_ram_addr=None
  ),
  "Jet Guillotine": MMXCMItemData(
    type="Weapon",
    code=60,
    classification=IC.useful,
    item_id=111,
    update_ram_addr=None
  ),
  "Beast Lancer": MMXCMItemData(
    type="Weapon",
    code=61,
    classification=IC.useful,
    item_id=112,
    update_ram_addr=None
  ),
  # Marino's Non-Progressive Weapons:
  "Vengeful Needles": MMXCMItemData(
    type="Weapon",
    code=62,
    classification=IC.useful,
    item_id=145,
    update_ram_addr=None
  ),
  "Beam Dagger": MMXCMItemData(
    type="Weapon",
    code=63,
    classification=IC.useful,
    item_id=133,
    update_ram_addr=None
  ),
  # Cinnamon's Non-Progressive Weapons:
  "Injector": MMXCMItemData(
    type="Weapon",
    code=64,
    classification=IC.useful,
    item_id=151,
    update_ram_addr=None
  ),
  "Drill Arm": MMXCMItemData(
    type="Weapon",
    code=65,
    classification=IC.useful,
    item_id=152,
    update_ram_addr=None
  ),
  "Melting Arm": MMXCMItemData(
    type="Weapon",
    code=66,
    classification=IC.useful,
    item_id=153,
    update_ram_addr=None
  ),
  "Head Hammer": MMXCMItemData(
    type="Weapon",
    code=67,
    classification=IC.useful,
    item_id=155,
    update_ram_addr=None
  ),
  "O Effecter": MMXCMItemData(
    type="Weapon",
    code=68,
    classification=IC.useful,
    item_id=159,
    update_ram_addr=None
  ),
  "Kitty Gloves": MMXCMItemData(
    type="Weapon",
    code=69,
    classification=IC.useful,
    item_id=160,
    update_ram_addr=None
  ),
  # Axl's Non-Progressive Weapons:
  "Insect Killer": MMXCMItemData(
    type="Weapon",
    code=70,
    classification=IC.useful,
    item_id=177,
    update_ram_addr=None
  ),
  "Noise Cancellor": MMXCMItemData(
    type="Weapon",
    code=71,
    classification=IC.useful,
    item_id=179,
    update_ram_addr=None
  ),
  "Beast Killer": MMXCMItemData(
    type="Weapon",
    code=72,
    classification=IC.useful,
    item_id=181,
    update_ram_addr=None
  ),
  "Preon Killer": MMXCMItemData(
    type="Weapon",
    code=73,
    classification=IC.useful,
    item_id=183,
    update_ram_addr=None
  ),
  "Manhunter": MMXCMItemData(
    type="Weapon",
    code=74,
    classification=IC.useful,
    item_id=185,
    update_ram_addr=None
  ),
  "Mettaur Crash": MMXCMItemData(
    type="Weapon",
    code=75,
    classification=IC.useful,
    item_id=186,
    update_ram_addr=None
  ),
  "Ancient Gun": MMXCMItemData(
    type="Weapon",
    code=76,
    classification=IC.useful,
    item_id=188,
    update_ram_addr=None

}

#This is the list for every Progressive Weapon separated by Character.
PROGRESSIVE_WEAPONS_TABLE: dict[str, list[MMXCMItemData]] = {
  # -----Progressive Weapons for X -----
  "X-Buster Progression": [
    MMXCMItemData(
      name="X Buster",
      type="Weapon",
      code=77,
      classification=IC.useful,
      item_id=25,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="X Buster MK II",
      type="Weapon",
      code=78,
      classification=IC.useful,
      item_id=33,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="X Buster MK III",
      type="Weapon",
      code=79,
      classification=IC.useful,
      item_id=47,
      update_ram_addr=None
    ),
  ],

  "Guard Buster Progression": [
    MMXCMItemData(
      name="Guard Buster",
      type="Weapon",
      code=80,
      classification=IC.useful,
      item_id=26,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Guard Buster MKII",
      type="Weapon",
      code=81,
      classification=IC.useful,
      item_id=31,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Guard Buster MKIII",
      type="Weapon",
      code=82,
      classification=IC.useful,
      item_id=41,
      update_ram_addr=None
    )
  ],
  
  "Fire Buster Progression": [
    MMXCMItemData(
      name="Fire Buster",
      type="Weapon",
      code=83,
      classification=IC.useful,
      item_id=27,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Fire Buster MK II",
      type="Weapon",
      code=84,
      classification=IC.useful,
      item_id=35,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Fire Buster MK III",
      type="Weapon",
      code=85,
      classification=IC.useful,
      item_id=44,
      update_ram_addr=None
    )
  ],

  "Thunder Buster Progression": [
    MMXCMItemData(
      name="Thunder Buster",
      type="Weapon",
      code=86,
      classification=IC.useful,
      item_id=28,
      update_ram_addr=None
    ), 
    MMXCMItemData(
      name="Thunder Buster MKII",
      type="Weapon",
      code=87,
      classification=IC.useful,
      item_id=37,
      update_ram_addr=None
    ), 
    MMXCMItemData(
      name="Thunder Buster MKIII",
      type="Weapon",
      code=88,
      classification=IC.useful,
      item_id=46,
      update_ram_addr=None
    )
  ],

  "Scope Buster Progression": [
    MMXCMItemData(
      name="Scope Buster",
      type="Weapon",
      code=89,
      classification=IC.useful,
      item_id=29,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Scope Buster MKII",
      type="Weapon",
      code=90,
      classification=IC.useful,
      item_id=38,
      update_ram_addr=None
    )
  ],

  "Ice Buster Progression": [
    MMXCMItemData(
      name="Ice Buster",
      type="Weapon",
      code=91,
      classification=IC.useful,
      item_id=30,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Ice Buster MKII",
      type="Weapon",
      code=92,
      classification=IC.useful,
      item_id=36,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Ice Buster MKIII",
      type="Weapon",
      code=93,
      classification=IC.useful,
      item_id=45,
      update_ram_addr=None
    )
  ],

  "Gatling Buster Progression": [
    MMXCMItemData(
      name="Gatling Buster",
      type="Weapon",
      code=94,
      classification=IC.useful,
      item_id=32,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Gatling Buster MKII",
      type="Weapon",
      code=95,
      classification=IC.useful,
      item_id=40,
      update_ram_addr=None
    )
  ],

  "Aero Buster Progression": [
    MMXCMItemData(
      name="Aero Buster",
      type="Weapon",
      code=96,
      classification=IC.useful,
      item_id=34,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Aero Buster MKII",
      type="Weapon",
      code=97,
      classification=IC.useful,
      item_id=42,
      update_ram_addr=None
    )
  ],

  "Limit Buster Progression": [
    MMXCMItemData(
      name="Limit Buster",
      type="Weapon",
      code=98,
      classification=IC.useful,
      item_id=39,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Limit Buster MKII",
      type="Weapon",
      code=99,
      classification=IC.useful,
      item_id=43,
      update_ram_addr=None
    )
  ],
  
  # -----Progressive Weapons For Zero Start Here-----
  "Z Saber Progression": [
    MMXCMItemData(
      name="Z Saber",
      type="Weapon",
      code=100,
      classification=IC.useful,
      item_id=50,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Z Saber+",
      type="Weapon",
      code=101,
      classification=IC.useful,
      item_id=51,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Z Saber++",
      type="Weapon",
      code=102,
      classification=IC.useful,
      item_id=58,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Z Saber+++",
      type="Weapon",
      code=103,
      classification=IC.useful,
      item_id=66,
      update_ram_addr=None
    )
  ],
  
  "Flame Saber Progression": [
    MMXCMItemData(
      name="Flame Saber",
      type="Weapon",
      code=104,
      classification=IC.useful,
      item_id=52,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Flame Saber+",
      type="Weapon",
      code=105,
      classification=IC.useful,
      item_id=62,
      update_ram_addr=None
    )
  ],
  "Ice Saber Progression": [
    MMXCMItemData(
      name="Ice Saber",
      type="Weapon",
      code=106,
      classification=IC.useful,
      item_id=53,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Ice Saber+",
      type="Weapon",
      code=107,
      classification=IC.useful,
      item_id=63,
      update_ram_addr=None
    )
  ],
  
  "Thunder Saber Progression": [
    MMXCMItemData(
      name="Thunder Saber",
      type="Weapon",
      code=108,
      classification=IC.useful,
      item_id=54,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Thunder Saber+",
      type="Weapon",
      code=109,
      classification=IC.useful,
      item_id=64,
      update_ram_addr=None
    )
  ],
  
  "Z Ichimonji Progression": [
    MMXCMItemData(
      name="Z Ichimonji",
      type="Weapon",
      code=110,
      classification=IC.useful,
      item_id=55,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Rei Ichimonji",
      type="Weapon",
      code=111,
      classification=IC.useful,
      item_id=65,
      update_ram_addr=None
    )
  ],

  "Z Rapier Progression": [
    MMXCMItemData(
      name="Z Rapier",
      type="Weapon",
      code=112,
      classification=IC.useful,
      item_id=56,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Z Rapier+",
      type="Weapon",
      code=113,
      classification=IC.useful,
      item_id=60,
      update_ram_addr=None
    )
  ],

  "Doubletooth Progression": [
    MMXCMItemData(
      name="Doubletooth",
      type="Weapon",
      code=114,
      classification=IC.useful,
      item_id=57,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Doubletooth+",
      type="Weapon",
      code=115,
      classification=IC.useful,
      item_id=61,
      update_ram_addr=None
    )
  ],

  # -----Progressive Weapons For Zero Start Here-----
  "Spades Progression": [
    MMXCMItemData(
      name="Jack of Spades",
      type="Weapon",
      code=116,
      classification=IC.useful,
      item_id=75,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Queen of Spades",
      type="Weapon",
      code=117,
      classification=IC.useful,
      item_id=79,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="King of Spades",
      type="Weapon",
      code=118,
      classification=IC.useful,
      item_id=83,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Ace of Spades",
      type="Weapon",
      code=119,
      classification=IC.useful,
      item_id=87,
      update_ram_addr=None
    )
  ],

  "Clubs Progression": [
    MMXCMItemData(
      name="Jack of Clubs",
      type="Weapon",
      code=120,
      classification=IC.useful,
      item_id=76,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Queen of Clubs",
      type="Weapon",
      code=121,
      classification=IC.useful,
      item_id=81,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="King of Clubs",
      type="Weapon",
      code=122,
      classification=IC.useful,
      item_id=84,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Ace of Clubs",
      type="Weapon",
      code=123,
      classification=IC.useful,
      item_id=88,
      update_ram_addr=None
    )
  ],

  "Diamonds Progression": [
    MMXCMItemData(
      name="Jack of Diamonds",
      type="Weapon",
      code=124,
      classification=IC.useful,
      item_id=77,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Queen of Diamonds",
      type="Weapon",
      code=125,
      classification=IC.useful,
      item_id=81,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="King of Diamonds",
      type="Weapon",
      code=126,
      classification=IC.useful,
      item_id=85,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Ace of Diamonds",
      type="Weapon",
      code=127,
      classification=IC.useful,
      item_id=89,
      update_ram_addr=None
    )
  ],

  "Hearts Progression": [
    MMXCMItemData(
      name="Jack of Hearts",
      type="Weapon",
      code=128,
      classification=IC.useful,
      item_id=78,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Queen of Hearts",
      type="Weapon",
      code=129,
      classification=IC.useful,
      item_id=82,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="King of Hearts",
      type="Weapon",
      code=130,
      classification=IC.useful,
      item_id=86,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Ace of Hearts",
      type="Weapon",
      code=131,
      classification=IC.useful,
      item_id=90,
      update_ram_addr=None
    )
  ],
  
# -----Progressive Weapons For Massimo Start Here-----
  "Massive Lance Progression": [
    MMXCMItemData(
      name="Massive Lance",
      type="Weapon",
      code=132,
      classification=IC.useful,
      item_id=100,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Massive Lance B",
      type="Weapon",
      code=133,
      classification=IC.useful,
      item_id=104,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Massive Lance Y",
      type="Weapon",
      code=134,
      classification=IC.useful,
      item_id=107,
      update_ram_addr=None
    )
  ],

  "Protect Lance Progression": [
    MMXCMItemData(
      name="Protect Lance",
      type="Weapon",
      code=135,
      classification=IC.useful,
      item_id=101,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Protect Lance B",
      type="Weapon",
      code=136,
      classification=IC.useful,
      item_id=105,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Protect Lance Y",
      type="Weapon",
      code=137,
      classification=IC.useful,
      item_id=109,
      update_ram_addr=None
    )
  ],

  "Crash Hammer Progression": [
    MMXCMItemData(
      name="Crash Hammer",
      type="Weapon",
      code=138,
      classification=IC.useful,
      item_id=102,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Crash Hammer B",
      type="Weapon",
      code=139,
      classification=IC.useful,
      item_id=106,
      update_ram_addr=None
    )
  ],
  
  "Shock Lance Progression": [
    MMXCMItemData(
      name="Shock Lance",
      type="Weapon",
      code=140,
      classification=IC.useful,
      item_id=103,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Shock Lance B",
      type="Weapon",
      code=141,
      classification=IC.useful,
      item_id=108,
      update_ram_addr=None
    )
  ],

# -----Progressive Weapons For Marino Start Here-----
  "Beam Knife Progression": [
    MMXCMItemData(
      name="Beam Knife",
      type="Weapon",
      code=142,
      classification=IC.useful,
      item_id=125,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Beam Dagger",
      type="Weapon",
      code=143,
      classification=IC.useful,
      item_id=132,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Beam Sword",
      type="Weapon",
      code=144,
      classification=IC.useful,
      item_id=136,
      update_ram_addr=None
  ],

  "Beam Chakram Progression": [
    MMXCMItemData(
      name="Beam Chakram",
      type="Weapon",
      code=145,
      classification=IC.useful,
      item_id=126,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Beam Chakram S",
      type="Weapon",
      code=146,
      classification=IC.useful,
      item_id=134,
      update_ram_addr=None 
    )
  ],

  "Beam Wonder Progression": [
    MMXCMItemData(
      name="Beam Wonder",
      type="Weapon",
      code=147,
      classification=IC.useful,
      item_id=127,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Beam Wonder S",
      type="Weapon",
      code=148,
      classification=IC.useful,
      item_id=135,
      update_ram_addr=None
    )
  ],

  "Fire Star Progression": [
    MMXCMItemData(
      name="Fire Star",
      type="Weapon",
      code=149,
      classification=IC.useful,
      item_id=128,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Fire Comet",
      type="Weapon",
      code=150,
      classification=IC.useful,
      item_id=138,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Fire Stella",
      type="Weapon",
      code=151,
      classification=IC.useful,
      item_id=142,
      update_ram_addr=None
    )
  ],

  "Ice Star Progression": [
    MMXCMItemData(
      name="Ice Star",
      type="Weapon",
      code=152,
      classification=IC.useful,
      item_id=129,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Ice Comet",
      type="Weapon",
      code=153,
      classification=IC.useful,
      item_id=139,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Ice Stella",
      type="Weapon",
      code=154,
      classification=IC.useful,
      item_id=143,
      update_ram_addr=None
    )
  ],

  "Thunder Star Progression": [
    MMXCMItemData(
      name="Thunder Star",
      type="Weapon",
      code=155,
      classification=IC.useful,
      item_id=130,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Thunder Comet",
      type="Weapon",
      code=156,
      classification=IC.useful,
      item_id=140,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Thunder Stella",
      type="Weapon",
      code=157,
      classification=IC.useful,
      item_id=144,
      update_ram_addr=None
    )
  ],
 # -----Progressive Weapons For Cinnamon Start Here-----
  "Hands Progression": [
    MMXCMItemData(
      name="Angel's Hand",
      type="Weapon",
      code=158,
      classification=IC.useful,
      item_id=150,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Archangel",
      type="Weapon",
      code=159,
      classification=IC.useful,
      item_id=154,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Divine Hand",
      type="Weapon",
      code=160,
      classification=IC.useful,
      item_id=156,
      update_ram_addr=None
    )
  ],

  "Boxer Progression": [
    MMXCMItemData(
      name="Metal Boxer",
      type="Weapon",
      code=161,
      classification=IC.useful,
      item_id=157,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Full Metal Boxer",
      type="Weapon",
      code=162,
      classification=IC.useful,
      item_id=158,
      update_ram_addr=None
    )
  ],

# -----Progressive Weapons For Axl Start Here-----
  "Axl Bullets Progression": [
    MMXCMItemData(
      name="Axl Bullets 1",
      type="Weapon",
      code=163,
      classification=IC.useful,
      item_id=175,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Axl Bullets 2",
      type="Weapon",
      code=164,
      classification=IC.useful,
      item_id=180,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Axl Bullets 3",
      type="Weapon",
      code=165,
      classification=IC.useful,
      item_id=184,
      update_ram_addr=None
    )
  ],

  "Barrels and Bullets Progression": [
    MMXCMItemData(
      name="Revolver Barrels",
      type="Weapon",
      code=166,
      classification=IC.useful,
      item_id=176,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Machine Bullets",
      type="Weapon",
      code=167,
      classification=IC.useful,
      item_id=178,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Machine Bullets 2",
      type="Weapon",
      code=168,
      classification=IC.useful,
      item_id=182,
      update_ram_addr=None
    ),
    MMXCMItemData(
      name="Auto Bullet",
      type="Weapon",
      code=169,
      classification=IC.useful,
      item_id=187,
      update_ram_addr=None
    )
  ],
}   

SUB_WEAPONS_TABLE: dict[str, MMXCMItemData] = {
  #All Sub-Weapons in the Game, Excluding Hyper Mode ones.
  "Micro Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=170,
    classification=IC.useful,
    item_id=1,
    update_ram_addr=None 
  ),
  "Tomahawk": MMXCMItemData(
    type="Sub-Weapon",
    code=171,
    classification=IC.useful,
    item_id=2,
    update_ram_addr=None
  ),
  "Twin Missiles": MMXCMItemData(
    type="Sub-Weapon",
    code=172,
    classification=IC.useful,
    item_id=3,
    update_ram_addr=None
  ),
  "Twin Tomahawks": MMXCMItemData(
    type="Sub-Weapon",
    code=173,
    classification=IC.useful,
    item_id=4,
    update_ram_addr=None
  ),
  "Force Missiles": MMXCMItemData(
    type="Sub-Weapon",
    code=174,
    classification=IC.useful,
    item_id=5,
    update_ram_addr=None
  ),
  "Force Tomahawks": MMXCMItemData(
    type="Sub-Weapon",
    code=175,
    classification=IC.useful,
    item_id=6,
    update_ram_addr=None
  ),
  "Hunter Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=176,
    classification=IC.useful,
    item_id=7,
    update_ram_addr=None
  ),
  "Photon Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=177,
    classification=IC.useful,
    item_id=8,
    update_ram_addr=None
  ),
  "Justice Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=178,
    classification=IC.useful,
    item_id=9,
    update_ram_addr=None
  ),
  "Fire Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=179,
    classification=IC.useful,
    item_id=10,
    update_ram_addr=None
  ),
  "Twin Fire": MMXCMItemData(
    type="Sub-Weapon",
    code=180,
    classification=IC.useful,
    item_id=11,
    update_ram_addr=None
  ),
  "Ice Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=181,
    classification=IC.useful,
    item_id=12,
    update_ram_addr=None
  ),
  "Twin Ice": MMXCMItemData(
    type="Sub-Weapon",
    code=182,
    classification=IC.useful,
    item_id=13,
    update_ram_addr=None
  ),
  "Thunder Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=183,
    classification=IC.useful,
    item_id=14,
    update_ram_addr=None
  ),
  "Twin Thunder": MMXCMItemData(
    type="Sub-Weapon",
    code=184,
    classification=IC.useful,
    item_id=15,
    update_ram_addr=None
  ),
  "Tractor Net": MMXCMItemData(
    type="Sub-Weapon",
    code=185,
    classification=IC.useful,
    item_id=16,
    update_ram_addr=None
  ),
  "Smoke Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=186,
    classification=IC.useful,
    item_id=17,
    update_ram_addr=None
  ),
  "Virus Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=187,
    classification=IC.useful,
    item_id=18,
    update_ram_addr=None
  ),
  "Cracker": MMXCMItemData(
    type="Sub-Weapon",
    code=188,
    classification=IC.useful,
    item_id=19,
    update_ram_addr=None
  ),
  "Cryogenic": MMXCMItemData(
    type="Sub-Weapon",
    code=189,
    classification=IC.useful,
    item_id=20,
    update_ram_addr=None
  ),
  "Get Zenny +": MMXCMItemData(
    type="Sub-Weapon",
    code=190,
    classification=IC.useful,
    item_id=21,
    update_ram_addr=None
  ),
  "Get EXP +": MMXCMItemData(
    type="Sub-Weapon",
    code=191,
    classification=IC.useful,
    item_id=22,
    update_ram_addr=None
  ),
  "Get FME +": MMXCMItemData(
    type="Sub-Weapon",
    code=192,
    classification=IC.useful,
    item_id=23,
    update_ram_addr=None
  ),
  "Rust Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=193,
    classification=IC.useful,
    item_id=24,
    update_ram_addr=None
  ),
  "Drill Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=194,
    classification=IC.useful,
    item_id=25,
    update_ram_addr=None
  ),
  "Melt Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=195,
    classification=IC.useful,
    item_id=26,
    update_ram_addr=None
  ),
  "Slime Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=196,
    classification=IC.useful,
    item_id=27,
    update_ram_addr=None
  ),
  "Oil Can": MMXCMItemData(
    type="Sub-Weapon",
    code=197,
    classification=IC.useful,
    item_id=28,
    update_ram_addr=None
  ),
  "Item Capture": MMXCMItemData(
    type="Sub-Weapon",
    code=198,
    classification=IC.useful,
    item_id=29,
    update_ram_addr=None
  ),
  "Energy Capture": MMXCMItemData(
    type="Sub-Weapon",
    code=199,
    classification=IC.useful,
    item_id=30,
    update_ram_addr=None
  ),
  "Power Capture": MMXCMItemData(
    type="Sub-Weapon",
    code=200,
    classification=IC.useful,
    item_id=31,
    update_ram_addr=None
  ),
  "Hawkeye": MMXCMItemData(
    type="Sub-Weapon",
    code=201,
    classification=IC.useful,
    item_id=32,
    update_ram_addr=None
  ),
  "Turbo Clock": MMXCMItemData(
    type="Sub-Weapon",
    code=202,
    classification=IC.useful,
    item_id=33,
    update_ram_addr=None
  ),
  "Heat Haze": MMXCMItemData(
    type="Sub-Weapon",
    code=203,
    classification=IC.useful,
    item_id=34,
    update_ram_addr=None
  ),
  "Generator": MMXCMItemData(
    type="Sub-Weapon",
    code=204,
    classification=IC.useful,
    item_id=35,
    update_ram_addr=None
  ),
  "Energy Field": MMXCMItemData(
    type="Sub-Weapon",
    code=205,
    classification=IC.useful,
    item_id=36,
    update_ram_addr=None
  ),
  "Bait": MMXCMItemData(
    type="Sub-Weapon",
    code=206,
    classification=IC.useful,
    item_id=37,
    update_ram_addr=None
  ),
  "Stamina Missile": MMXCMItemData(
    type="Sub-Weapon",
    code=207,
    classification=IC.useful,
    item_id=38,
    update_ram_addr=None
  ),
  "Vitality Missiles": MMXCMItemData(
    type="Sub-Weapon",
    code=208,
    classification=IC.useful,
    item_id=39,
    update_ram_addr=None
  ),
  "Combat Absorber": MMXCMItemData(
    type="Sub-Weapon",
    code=209,
    classification=IC.useful,
    item_id=40,
    update_ram_addr=None
  ),
  "Shot Absorber": MMXCMItemData(
    type="Sub-Weapon",
    code=210,
    classification=IC.useful,
    item_id=41,
    update_ram_addr=None
  ),
  "Super Absorber": MMXCMItemData(
    type="Sub-Weapon",
    code=211,
    classification=IC.useful,
    item_id=42,
    update_ram_addr=None
  ),
  "Vengeful Counter": MMXCMItemData(
    type="Sub-Weapon",
    code=212,
    classification=IC.useful,
    item_id=43,
    update_ram_addr=None
  )    
}


FORCE_METAL_TABLE: dict[str, MMXCMItemData] = {
  "Massimo Plus": MMXCMItemData(
    type="Force Metal",
    code=213,
    classification=IC.useful,
    item_id=34,
    update_ram_addr=None
  ),
  "Assassin Mind": MMXCMItemData(
    type="Force Metal",
    code=214,
    classification=IC.useful,
    item_id=35,
    update_ram_addr=None
  ),
  "Eagle Eye": MMXCMItemData(
    type="Force Metal",
    code=215,
    classification=IC.useful,
    item_id=36,
    update_ram_addr=None
  ),
  "Fat Slicer": MMXCMItemData(
    type="Force Metal",
    code=216,
    classification=IC.useful,
    item_id=37,
    update_ram_addr=None
  ),
  "Light As A Feather": MMXCMItemData(
    type="Force Metal",
    code=217,
    classification=IC.useful,
    item_id=38,
    update_ram_addr=None
  ),
  "SFM Fragment A": MMXCMItemData(
    type="Force Metal",
    code=218,
    classification=IC.useful,
    item_id=39,
    update_ram_addr=None
  ),
  "SFM Fragment B": MMXCMItemData(
    type="Force Metal",
    code=219,
    classification=IC.useful,
    item_id=40,
    update_ram_addr=None
  ),
  "Auto Sub Tank": MMXCMItemData(
    type="Force Metal",
    code=220,
    classification=IC.useful,
    item_id=69,
    update_ram_addr=None
  ),
  "Auto Recover": MMXCMItemData(
    type="Force Metal",
    code=221,
    classification=IC.useful,
    item_id=70,
    update_ram_addr=None
  ),
  "Auto Barrier": MMXCMItemData(
    type="Force Metal",
    code=222,
    classification=IC.useful,
    item_id=71,
    update_ram_addr=None
  ),
  "Bluff": MMXCMItemData(
    type="Force Metal",
    code=223,
    classification=IC.useful,
    item_id=72,
    update_ram_addr=None
  ),
  "ZERO Shift": MMXCMItemData(
    type="Force Metal",
    code=224,
    classification=IC.useful,
    item_id=73,
    update_ram_addr=None
  ),
  "X Heart": MMXCMItemData(
    type="Force Metal",
    code=225,
    classification=IC.useful,
    item_id=74,
    update_ram_addr=None
  ),
  "Decoy": MMXCMItemData(
    type="Force Metal",
    code=226,
    classification=IC.useful,
    item_id=75,
    update_ram_addr=None
  ),
  "Parry Impact": MMXCMItemData(
    type="Force Metal",
    code=227,
    classification=IC.useful,
    item_id=76,
    update_ram_addr=None
  ),
  "End To All": MMXCMItemData(
    type="Force Metal",
    code=228,
    classification=IC.useful,
    item_id=77,
    update_ram_addr=None
  ),
  "FS Canceller": MMXCMItemData(
    type="Force Metal",
    code=229,
    classification=IC.useful,
    item_id=78,
    update_ram_addr=None
  ),
  "Analyzer": MMXCMItemData(
    type="Force Metal",
    code=230,
    classification=IC.useful,
    item_id=79,
    update_ram_addr=None
  ),
  "Learning Aid": MMXCMItemData(
    type="Force Metal",
    code=231,
    classification=IC.useful,
    item_id=80,
    update_ram_addr=None
  ),
  "Caution": MMXCMItemData(
    type="Force Metal",
    code=232,
    classification=IC.useful,
    item_id=81,
    update_ram_addr=None
  ),
  "Attractor": MMXCMItemData(
    type="Force Metal",
    code=233,
    classification=IC.useful,
    item_id=82,
    update_ram_addr=None
  ),
  "Initiative": MMXCMItemData(
    type="Force Metal",
    code=234,
    classification=IC.useful,
    item_id=83,
    update_ram_addr=None
  ),
  "Self-repair": MMXCMItemData(
    type="Force Metal",
    code=235,
    classification=IC.useful,
    item_id=87,
    update_ram_addr=None
  ),
  "Exodus": MMXCMItemData(
    type="Force Metal",
    code=236,
    classification=IC.useful,
    item_id=88,
    update_ram_addr=None
  ),
  "Cutting Edge": MMXCMItemData(
    type="Force Metal",
    code=237,
    classification=IC.useful,
    item_id=89,
    update_ram_addr=None
  ),
  "Lucky Girl": MMXCMItemData(
    type="Force Metal",
    code=238,
    classification=IC.useful,
    item_id=90,
    update_ram_addr=None
  ),
  "Good Luck": MMXCMItemData(
    type="Force Metal",
    code=239,
    classification=IC.useful,
    item_id=91,
    update_ram_addr=None
  ),
  "Monopoly": MMXCMItemData(
    type="Force Metal",
    code=240,
    classification=IC.useful,
    item_id=92,
    update_ram_addr=None
  )
}

PROGRESSIVE_FORCE_METAL_TABLE: dict[str, MMXCMItemData] = {}
MECHANILOID_ITEMS_TABLE: dict[str, MMXCMItemData] = {}

#Add any other tables here, Filler, Trap, etc.
COLLECTIBLE_TABLE: dict[str, MMXCMItemData] = {}

#This is where all of the item tables are listed into one Dictionary.
ALL_ITEMS_TABLE = {
  **PROGRESSION_ITEM_TABLE,
  **USEFUL_ITEM_TABLE,
  **FILLER_TABLE,
  **WEAPONS_TABLE,
  **{item.name: item for item_list in PROGRESSIVE_WEAPONS_TABLE.values() for item in item_list},
  **SUB_WEAPONS_TABLE,
  **FORCE_METAL_TABLE,
  **COLLECTIBLE_TABLE

}
  
      
    
  
