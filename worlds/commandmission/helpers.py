from typing import NamedTuple, Optional 

class MMXCMRamData(NamedTuple):
    ram_addr: Optional[int] = None
    bit_position: Optional[int] = None
    ram_byte_size: Optional[int] = None
    pointer_offset: Optional[int] = None
    item_count: Optional[int] = None

REBELLION_MEDALS_DATA = {
    "Rebellion Medal (Lagrano Ruins)": {"address": 0x804A2109, "bit": 2},
    "Rebellion Medal (Central Tower)": {"address": 0x804A2109, "bit": 3},
    "Rebellion Medal (Tianna Camp)": {"address": 0x804A2109, "bit": 4},
    "Rebellion Medal (Gaudile Laboratory)": {"address": 0x804A2109, "bit": 5},
    "Rebellion Medal (Ulfat Factory)": {"address": 0x804A2109, "bit": 6},
    "Rebellion Medal (Gimialla Mine)": {"address": 0x804A2109, "bit": 7},
    "Rebellion Medal (Vanallia Desert)": {"address": 0x804A210A, "bit": 0},
    "Rebellion Medal (Melda Ore Plant)": {"address": 0x804A210A, "bit": 1},
    "Rebellion Medal (Grave Ruins Base)": {"address": 0x804A210A, "bit": 2},
}

ACCESS_CODES_DATA = {
    "Lagrano Ruins Access Code": {"address": 0x804A2108, "bit": 0},
    "Central Tower Access Code": {"address": 0x804A2108, "bit": 1},
    "Tianna Camp Access Code": {"address": 0x804A2108, "bit": 2},
    "Gaudile Laboratory Access Code": {"address": 0x804A2108, "bit": 3},
    "Ulfat Factory Access Code": {"address": 0x804A2108, "bit": 4},
    "Gimialla Mine Access Code": {"address": 0x804A2108, "bit": 5},
    "Vanallia Desert Access Code": {"address": 0x804A2108, "bit": 6},
    "Melda Ore Plant Access Code": {"address": 0x804A2108, "bit": 7},
    "Grave Ruins Base Access Code": {"address": 0x804A2109, "bit": 0},
    "Far East HQ Access Code": {"address": 0x804A2109, "bit": 1},
}
    
