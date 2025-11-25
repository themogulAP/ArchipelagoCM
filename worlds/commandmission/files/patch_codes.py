import dolphin_memory_engine as dolphin
from CommonClient import logger
from typing import Callable, Dict

# Define the type for the patching function for clarity
PatchFunction = Callable[[], None]

# --- Individual Access Code Patching Functions ---

def patch_lagrano_ruins():
    """Patches RAM for Lagrano Ruins Access Code."""
    # Write the first PowerPC instruction. (0x80082fa4)
    dolphin.write_bytes(0x80082fa4, b'\x3c\x80\x00\x01')
    # Write the second PowerPC instruction. (0x80082fac)
    dolphin.write_bytes(0x80082fac, b'\x38\x04\x03\x46')

def patch_central_tower():
    """Patches RAM for Central Tower Access Code.
    We need to only target the BIT POSITION to open the blockers... or it is a problem for chapter 2."""

    BLOCKER_ADDR = 0x804A20C1
    BIT_POSITION = 0

    try:
        # 1. Read the bytes at the Blocker Address
        current_value_bytes = dolphin.read_bytes(BLOCKER_ADDR, 1)
        current_value = int.from_bytes(current_value_bytes, 'big')

        # 2. Modify and set Bit position 0 with (bitwise OR)
        new_value = current_value | (1 << BIT_POSITION)

        # 3. Write modified byte back to RAM
        dolphin.write_bytes(BLOCKER_ADDR, new_value.to_bytes(1, 'big'))

    except Exception as e:
        logger.error(f"Error applying read and write patch (0x{BLOCKER_ADDR}, Bit: 0): {e}")

def patch_tianna_camp():
    """Patches RAM for Tianna Camp Access Code."""
    # Write the first PowerPC instruction. (0x80082fcc)
    dolphin.write_bytes(0x80082fcc, b'\x3c\x80\x00\x03')
    # Write the second PowerPC instruction. (0x80082fd4)
    dolphin.write_bytes(0x80082fd4, b'\x38\x04\x01\x41')

def patch_gaudile_laboratory():
    """Patches RAM for Gaudile Laboratory Access Code."""
    # Write the first PowerPC instruction. (0x80082ff4)
    dolphin.write_bytes(0x80082ff4, b'\x3c\x80\x00\x04')
    # Write the second PowerPC instruction. (0x80082ffC)
    dolphin.write_bytes(0x80082ffC, b'\x38\x04\x01\x41')

def patch_ulfat_factory():
    """Patches RAM for Ulfat Factory Access Code."""
    # Write the first PowerPC instruction. (0x8008301c)
    dolphin.write_bytes(0x8008301c, b'\x3c\x80\x00\x05')
    # Write the second PowerPC instruction. (0x80083024)
    dolphin.write_bytes(0x80083024, b'\x38\x04\x01\x41')

def patch_gimialla_mine():
    """Patches RAM for Gimialla Mine Access Code."""
    # Write the first PowerPC instruction. (0x80083044)
    dolphin.write_bytes(0x80083044, b'\x3c\x80\x00\x06')
    # Write the second PowerPC instruction. (0x8008304c)
    dolphin.write_bytes(0x8008304c, b'\x38\x04\x01\x41')

def patch_vanallia_desert():
    """Patches RAM for Vanallia Desert Access Code."""
    # Write the first PowerPC instruction. (0x8008306c)
    dolphin.write_bytes(0x8008306c, b'\x3c\x80\x00\x07')
    # Write the second PowerPC instruction. (0x80083074)
    dolphin.write_bytes(0x80083074, b'\x38\x04\x01\x41')

def patch_melda_ore_plant():
    """Patches RAM for Melda Ore Plant Access Code."""
    # Write the first PowerPC instruction. (0x80083094)
    dolphin.write_bytes(0x80083094, b'\x3c\x80\x00\x08')
    # Write the second PowerPC instruction. (0x8008309c)
    dolphin.write_bytes(0x8008309c, b'\x38\x04\x01\x41')

def patch_grave_ruins_base():
    """Patches RAM for Grave Ruins Base Access Code."""
    # Write the first PowerPC instruction. (0x800830bc)
    dolphin.write_bytes(0x800830bc, b'\x3c\x80\x00\x09')
    # Write the second PowerPC instruction. (0x800830c4)
    dolphin.write_bytes(0x800830c4, b'\x38\x04\x01\x41')

# --- Mapping Dictionary ---

ACCESS_CODE_PATCHES: Dict[str, PatchFunction] = {
    "Lagrano Ruins Access Code": patch_lagrano_ruins,
    "Central Tower Access Code": patch_central_tower,
    "Tianna Camp Access Code": patch_tianna_camp,
    "Gaudile Laboratory Access Code": patch_gaudile_laboratory,
    "Ulfat Factory Access Code": patch_ulfat_factory,
    "Gimialla Mine Access Code": patch_gimialla_mine,
    "Vanallia Desert Access Code": patch_vanallia_desert,
    "Melda Ore Plant Access Code": patch_melda_ore_plant,
    "Grave Ruins Base Access Code": patch_grave_ruins_base,
}