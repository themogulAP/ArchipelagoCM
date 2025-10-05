# --- RAM Monitor Addresses ---
# Address used for reading the current screen selection/game state
SCREEN_SELECT_ADDRESS = 0x804A208B
# Address used for reading the current cutscene ID (for medal checks)
CUTSCENE_ID_ADDRESS = 0x804A208F
# Address used for reading the current room ID (for Medal 9 check)
ROOM_ID_ADDRESS = 0x804A2083
# Address used for checking the specific room exit state for the Big 4 revert logic
REVERT_STATE_ADDRESS = 0x804A208E

# --- Rebellion Medal Location Checks ---
REBELLION_MEDAL_CHECKS = {
    0x05: "Rebellion Medal 1", # Lagrano Ruins Clear
    0x12: "Rebellion Medal 2", # Central Tower Clear...
    0x1B: "Rebellion Medal 3",
    0x26: "Rebellion Medal 4",
    0x2D: "Rebellion Medal 5",
    0x37: "Rebellion Medal 6",
    0x3E: "Rebellion Medal 7",
    0x4A: "Rebellion Medal 8",
}
GRAVE_RUINS_MEDAL = "Rebellion Medal 9"


# --- PowerPC Patches for "The Big 4" ---
# Addresses
GAMEPLAY_STATE_SET_ADDR = 0x80054b20
GAMEPLAY_STATE_STORE_ADDR = 0x80054b24
STAGE_SET_ADDR = 0x80054b28
AREA_SET_ADDR = 0x80054b2C

# Original/Revert Values (Vanilla)
GAMEPLAY_SET_VANILLA = b'\x38\x60\x00\x00'  # li r3, 0
GAMEPLAY_STORE_VANILLA = b'\xfc\x40\x08\x90'  # fmr f2, f1
STAGE_VANILLA = b'\x38\x80\x00\x01'  # li r4, 1
AREA_VANILLA = b'\x80\x1f\x00\x68'  # lwz r0,0x0068(r31)

# Shared Patch Values (The first 3 lines for ALL medals)
GAMEPLAY_PATCH = b'\x38\x00\x00\x07'  # li r0, 7
GAMEPLAY_STORE_PATCH = b'\x90\x1a\x00\x28'  # stw r0, 0x0028(r26)
STAGE_PATCH = b'\x3c\x00\x00\x02'  # lis r0, 0x0002

# Unique 4th Patch Values
ARCADE_PATCH = b'\x60\x00\x05\x4c'  # For Medals 1, 3-9 (ori r0, 0x054C)
HELIPAD_PATCH = b'\x60\x00\x15\x53'  # For Medal 2 (ori r0, 0x1553)