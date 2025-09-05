from typing import NamedTuple, Dict, Set

from BaseClasses import Item
from BaseClasses import ItemClassification as IC 

# This will import from the Helpers.py in the same folder. 
from .Helpers import MMXCMRamData

# This will start our 'blueprint' for Mega Man X Command Mission items! 
class MMXCMItemData(NamedTuple):
  type: str
  code: Optional[int]
  classification: IC
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
  ),
  
      
    
  
