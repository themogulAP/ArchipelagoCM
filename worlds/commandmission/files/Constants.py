# --- RAM Monitor Addresses ---
# Address used for reading the current screen selection/game state
SCREEN_SELECT_ADDRESS = 0x804A208B
# Address used for reading the current cutscene ID (for medal checks)
CUTSCENE_ID_ADDRESS = 0x804A208F
# Address used for checking the specific room exit state for the Big 4 revert logic
REVERT_STATE_ADDRESS = 0x804A208E

WAIT_TIMER_SHORT_TIMEOUT: float = 0.125

# --- Rebellion Medal Location Checks ---
REBELLION_MEDAL_CHECKS = {
    0x04: "Rebellion Medal 1", # Lagrano Ruins Clear
    0x11: "Rebellion Medal 2", # Central Tower Clear...
    0x1A: "Rebellion Medal 3",
    0x25: "Rebellion Medal 4",
    0x2C: "Rebellion Medal 5",
    0x36: "Rebellion Medal 6",
    0x3D: "Rebellion Medal 7",
    0x49: "Rebellion Medal 8",
    0x51: "Rebellion Medal 9"
}

# --- PowerPC Patches for "The Big 4" ---
# Addresses
GAMEPLAY_STATE_SET_ADDR = 0x8001050C
GAMEPLAY_STATE_STORE_ADDR = 0x80010510
STAGE_SET_ADDR = 0x80010514
AREA_SET_ADDR = 0x80010518

# Original/Revert Values (Vanilla)
GAMEPLAY_SET_VANILLA = b'\x7c\x84\x02\x14'  # add r4, r4, r0
GAMEPLAY_STORE_VANILLA = b'\x80\x64\x00\x04'  # lwz r3, 0x0004 (r4)
STAGE_VANILLA = b'\x80\x04\x00\x08'  # lwz r0, 0x0008 (r4)
AREA_VANILLA = b'\x90\x65\x00\x28'  # stw r3, 0x0028 (r5)

# Shared Patch Values (The first 3 lines for ALL medals)
GAMEPLAY_PATCH = b'\x38\x60\x00\x07'  # li r3, 7
GAMEPLAY_STORE_PATCH = b'\x90\x65\x00\x28'  # stw r3, 0x0028(r26)
STAGE_PATCH = b'\x3c\x00\x00\x02'  # lis r0, 0x0002

# Unique 4th Patch Values
ARCADE_PATCH = b'\x60\x00\x05\x4c'  # For Medals 1, 3-9 (ori r0, 0x054C)
HELIPAD_PATCH = b'\x60\x00\x15\x53'  # For Medal 2 (ori r0, 0x1553)

# ------------ Character ROSTER Addresses ------------------
PARTY_COUNT_ADDR = 0x804A3294
ROSTER_BASE_ADDR = 0x804A3295