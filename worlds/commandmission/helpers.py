from typing import NamedTuple, Optional, Any

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
    
def write_bit_to_ram(address: int, bit_position: int, dolphin_instance):
    """
    Reads a byte from a RAM address, sets a specific bit, and then writes the byte back.
    This is used for triggering in-game events.

    :param address: The RAM address to modify.
    :param bit_position: The bit to set (0-7).
    :param dolphin_instance: The dolphin_memory_engine instance.
    """
    try:
        # Read the current byte at the address
        current_value_bytes = dolphin_instance.read_bytes(address, 1)
        current_value = current_value_bytes[0]

        # Set the specified bit to 1
        new_value = current_value | (1 << bit_position)

        # Write the new byte back to the address
        dolphin_instance.write_bytes(address, new_value.to_bytes(1, byteorder='big'))

        print(f"Successfully set bit {bit_position} at address {hex(address)}")

    except Exception as e:
        print(f"Error writing to RAM at address {hex(address)}: {e}")
