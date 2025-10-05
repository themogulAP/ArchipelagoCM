import dolphin_memory_engine as dolphin
from CommonClient import logger
from typing import Callable, Dict

# Define the type for the patching function for clarity
PatchFunction = Callable[[], None]

# --- Individual Access Code Patching Functions ---

def patch_lagrano_ruins():
    """Patches RAM for Lagrano Ruins Access Code."""
    logger.info("Patching RAM to enable Lagrano Ruins teleporter.")
    # Write the first PowerPC instruction. (0x80082fa4)
    dolphin.write_bytes(0x80082fa4, b'\x3c\x80\x00\x01')
    # Write the second PowerPC instruction. (0x80082fac)
    dolphin.write_bytes(0x80082fac, b'\x38\x08\x03\x46')

def patch_central_tower():
    """Patches RAM for Central Tower Access Code."""
    logger.info("Changing RAM value to remove Central Tower cutscene and Aile blockers.")
    # Write a single byte with a value of 0 - removes cutscene blockers. (0x804A20BD)
    dolphin.write_bytes(0x804A20BD, b'\x00')
    # Write a single byte with a value of 1 - removes Aile Blocker. (0x804A20C1)
    dolphin.write_bytes(0x804A20C1, b'\x01')

def patch_tianna_camp():
    """Patches RAM for Tianna Camp Access Code."""
    logger.info("Patching RAM to enable Tianna Camp teleporter.")
    # Write the first PowerPC instruction. (0x80082fcc)
    dolphin.write_bytes(0x80082fcc, b'\x3c\x80\x00\x03')
    # Write the second PowerPC instruction. (0x80082fd4)
    dolphin.write_bytes(0x80082fd4, b'\x38\x04\x01\x41')

def patch_gaudile_laboratory():
    """Patches RAM for Gaudile Laboratory Access Code."""
    logger.info("Patching RAM to enable Gaudile Laboratory teleporter.")
    # Write the first PowerPC instruction. (0x80082ff4)
    dolphin.write_bytes(0x80082ff4, b'\x3c\x80\x00\x04')
    # Write the second PowerPC instruction. (0x80082ffC)
    dolphin.write_bytes(0x80082ffC, b'\x38\x04\x01\x41')

def patch_ulfat_factory():
    """Patches RAM for Ulfat Factory Access Code."""
    logger.info("Patching RAM to enable Ulfat Factory teleporter.")
    # Write the first PowerPC instruction. (0x8008301c)
    dolphin.write_bytes(0x8008301c, b'\x3c\x80\x00\x05')
    # Write the second PowerPC instruction. (0x80083024)
    dolphin.write_bytes(0x80083024, b'\x38\x04\x01\x41')

def patch_gimialla_mine():
    """Patches RAM for Gimialla Mine Access Code."""
    logger.info("Patching RAM to enable Gimialla Mine teleporter.")
    # Write the first PowerPC instruction. (0x80083044)
    dolphin.write_bytes(0x80083044, b'\x3c\x80\x00\x06')
    # Write the second PowerPC instruction. (0x8008304c)
    dolphin.write_bytes(0x8008304c, b'\x38\x04\x01\x41')

def patch_vanallia_desert():
    """Patches RAM for Vanallia Desert Access Code."""
    logger.info("Patching RAM to enable Vanallia Desert teleporter.")
    # Write the first PowerPC instruction. (0x8008306c)
    dolphin.write_bytes(0x8008306c, b'\x3c\x80\x00\x07')
    # Write the second PowerPC instruction. (0x80083074)
    dolphin.write_bytes(0x80083074, b'\x38\x04\x01\x41')

def patch_melda_ore_plant():
    """Patches RAM for Melda Ore Plant Access Code."""
    logger.info("Patching RAM to enable Melda Ore Plant teleporter.")
    # Write the first PowerPC instruction. (0x80083094)
    dolphin.write_bytes(0x80083094, b'\x3c\x80\x00\x08')
    # Write the second PowerPC instruction. (0x8008309c)
    dolphin.write_bytes(0x8008309c, b'\x38\x04\x01\x41')

def patch_grave_ruins_base():
    """Patches RAM for Grave Ruins Base Access Code."""
    logger.info("Patching RAM to enable Grave Ruins Base teleporter.")
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