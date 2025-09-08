from typing import NamedTuple, Dict, Optional, Set

from BaseClasses import Item
from BaseClasses import ItemClassification as IC 

# This will import from the Helpers.py in the same folder. 
from .Helpers import MMXCMRamData

# This will start our 'blueprint' for Mega Man X Command Mission items! 
class MMXCMItemData(NamedTuple):
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

#Add any other tables here, Filler, Trap, etc.
COLLECTIBLE_TABLE: dict[str, MMXCMItemData] = {}

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

#This is where all of the item tables are listed into one Dictionary.
ALL_ITEMS_TABLE = {
  **PROGRESSION_ITEM_TABLE,
  **USEFUL_ITEM_TABLE,
  **COLLECTIBLE_TABLE,
  **FILLER_TABLE,
}
  
      
    
  
