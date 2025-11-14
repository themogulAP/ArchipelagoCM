"""This file will hold ALL the initial parameters for characters upon getting them in vanilla.
For Example: Zero will be level 18 when you acquire him, like out of chapter 5."""

# Base RAM address for Zero's data block.
# This address will be used as the anchor for all offsets below when injecting data.
X_SLOT_BASE_ADDRESS = 0x804A2CAB
ZERO_SLOT_BASE_ADDRESS = 0x804A2D7F
SPIDER_SLOT_BASE_ADDRESS = 0x804A2E53
MASSIMO_SLOT_BASE_ADDRESS = 0x804A2F27
MARINO_SLOT_BASE_ADDRESS = 0x804A2FFB
CINNAMON_SLOT_BASE_ADDRESS = 0x804A30CF
AXL_SLOT_BASE_ADDRESS = 0x804A31A3
# Note that Offsets below are RELATIVE to the character's Base Address.

# --- ZERO'S VANILLA PARAMETER DATA ---
# Format: (OFFSET_FROM_BASE_ADDRESS, VANILLA_DECIMAL_VALUE)
# This list is used by AP and our Client to write the exact starting state
# for Zero when he is acquired via an Archipelago check.

X_VANILLA_PARAMS = [
    # ------------------ Level/ID ------------------
    (0x00, 11),    # X's Lvl String (804A2CAB)
    (0x04, 0),    # Character Picture (ID) (804A2CAF)

    # ------------------ EXP ------------------
    (0x07, 10),    # # of 255's Total EXP (804A2CB2)
    (0x08, 80),    # Total EXP # (804A2CB3)

    # ------------------ HP ------------------
    (0x0B, 4),    # # of 255's HP Current (804A2CB6)
    (0x0C, 251),   # Current HP (804A2CB7)
    (0x0F, 4),    # # of 255's Max HP (804A2CBA)
    (0x10, 251),   # Max HP (804A2CBB)
    (0x13, 4),    # # of 255's Actual HP (804A2CBE)
    (0x14, 251),   # Actual HP (804A2CBF)

    # ------------------ WE/Core Stats ------------------
    (0x18, 25),   # Initial WE (804A2CC3)
    (0x1C, 25),   # WE Per Turn (804A2CC7)
    (0x20, 55),   # Power Stat (804A2CCB)
    (0x24, 34),   # Armor Stat (804A2CCF)
    (0x28, 33),   # Shield Stat (804A2CD3)
    (0x2C, 41),   # Speed Stat (804A2CD7)
    (0x34, 100),  # Accuracy? (804A2CDF)
    (0x40, 2),    # Crit Chance (804A2CEB)

    # ------------------ Resistances ------------------
    (0x5C, 2),    # Combat Resistance (804A2D07)
    (0x60, 2),    # Shot Resistance (804A2D0B)
    (0x6C, 2),    # Fire Resistance (804A2D17)
    (0x70, 2),    # Water Resistance (804A2D1B)
    (0x74, 2),    # Thunder Resistance (804A2D1F)

    # ------------------ EQUIPMENT/FM ------------------
    (0xB6, 25),   # X's Weapon (804A2D61)
    (0xB8, 1),    # Sub Weapon X (804A2D63)
    (0xBA, 1),    # Sub Weapon Y (804A2D65)
    (0xBC, 4),    # Erosion Slots (804A2D67)
    (0xBD, 255),  # Is Force Metal #1 On? (804A2D68)
    (0xBE, 255),  # Force Metal #1 (804A2D69)
    (0xBF, 255),  # Is Force Metal #2 On? (804A2D6A)
    (0xC0, 255),  # Force Metal #2 (804A2D6B)
    (0xC1, 255),  # Is Force Metal #3 On? (804A2D6C)
    (0xC2, 255),  # Force Metal #3 (804A2D6D)
    (0xC3, 255),  # Is Force Metal #4 On? (804A2D6E)
    (0xC4, 255),  # Force Metal #4 (804A2D6F)

    # ------------------ Hyper Mode ------------------
    (0xC8, 10),   # Current Erosion (804A2D73)
    (0xCE, 6),    # Current Hyper Mode (804A2D79)
    (0xD0, 6),    # Max Hyper Mode (804A2D7B)
]

ZERO_VANILLA_PARAMS = [
    # ------------------ Level/ID  ------------------
    (0x00, 18),  # Zero's Level String (804A2D7F)
    (0x04, 1),  # Character Picture (ID) (804A2D83)

    # ------------------ EXP  ------------------
    (0x07, 47),  # # of 255's EXP (804A2D86)
    (0x08, 118),  # Total EXP # (804A2D87)

    # ------------------ HP  ------------------
    (0x0B, 8),  # # of 255's Current HP (804A2D8A)
    (0x0C, 171),  # Current HP (804A2D8B)
    (0x0F, 8),  # # of 255's MAX HP (804A2D8E)
    (0x10, 171),  # Max HP (804A2D8F)
    (0x13, 8),  # # of 255's Actual HP (804A2D92)
    (0x14, 171),  # Actual HP (804A2D93)

    # ------------------ WE/Core Stats  ------------------
    (0x18, 15),  # Initial WE (804A2D97)
    (0x1C, 25),  # WE Gained Per Turn (804A2D9B)
    (0x20, 93),  # Power Stat (804A2D9F)
    (0x24, 49),  # Armor Stat (804A2DA3)
    (0x28, 48),  # Shield Stat (804A2DA7)
    (0x2C, 44),  # Speed Stat (804A2DAB)
    (0x34, 98),  # Accuracy? (804A2DB3)
    (0x40, 3),  # Crit Chance (804A2DBF)

    # ------------------ Resistances  ------------------
    (0x5C, 2),  # Combat Resistance (804A2DDB)
    (0x60, 2),  # Shot Resistance (804A2DDF)
    (0x6C, 2),  # Fire Resistance (804A2DEB)
    (0x70, 2),  # Water Resistance (804A2DEF)
    (0x74, 2),  # Thunder Resistance (804A2DF3)

    # ------------------ EQUIPMENT/FM ------------------
    (0xB6, 51),  # Zero's Weapon (804A2E35)
    (0xB8, 34),  # Sub Weapon X (804A2E37)
    (0xBA, 34),  # Sub Weapon Y (804A2E39)
    (0xBC, 3),  # Erosion Slots (804A2E3B)
    (0xBD, 255),  # Is Force Metal #1 ON? (804A2E3C)
    (0xBE, 255),  # Force Metal #1 (804A2E3D)
    (0xBF, 255),  # Is Force Metal #2 ON? (804A2E3E)
    (0xC0, 255),  # Force Metal #2 (804A2E3F)
    (0xC1, 255),  # Is Force Metal #3 On? (804A2E40)
    (0xC2, 255),  # Force Metal #3 (804A2E41)
    (0xC3, 255),  # Is Force Metal #4 On? (804A2E42)
    (0xC4, 255),  # Force Metal #4 (804A2E43)

    # ------------------ Hyper Mode  ------------------
    (0xC8, 13),  # Current Erosion (804A2E47)
    (0xCE, 3),  # Current Hyper Mode (804A2E4D)
    (0xD0, 3),  # Max Hyper Mode (804A2E4F)
    # ------------------ Action Trigger -----------------
    (0x4F4, 0)  # Zero's Action Trigger Upgrade (804A3277)
]

# --- SPIDER'S VANILLA PARAMETER DATA (CORRECTED) ---
SPIDER_VANILLA_PARAMS = [
    # Level/ID
    (0x00, 9),  # Current Level Slot 2 (804A2E53)
    (0x04, 2),  # Character Picture (ID) (804A2E57)

    # EXP
    (0x07, 4),  # # of 255's Total EXP (804A2E5A)
    (0x08, 76),  # Total Exp # (804A2E5B)

    # HP (Values corrected from -91 to 165)
    (0x0B, 4),  # # of 255's HP (Current) (804A2E5E)
    (0x0C, 165),  # Current HP (804A2E5F)
    (0x0F, 4),  # # of 255's HP (Max) (804A2E62)
    (0x10, 165),  # Max HP (804A2E63)
    (0x13, 4),  # # of 255's ACTUAL HP (804A2E66)
    (0x14, 165),  # ACTUAL HP Value (804A2E67)

    # WE/Core Stats
    (0x18, 40),  # Initial WE (804A2E6B)
    (0x1C, 25),  # WE Per Turn (804A2E6F)
    (0x20, 40),  # Power Slot2 (804A2E73)
    (0x24, 23),  # Armor Slot2 (804A2E77)
    (0x28, 32),  # Shield Slot 2 (804A2E7B)
    (0x2C, 39),  # Speed Slot 2 (804A2E7F)
    (0x34, 100),  # Accuracy (804A2E87)
    (0x40, 6),  # Crit Chance (804A2E93)

    # Resistances
    (0x5C, 2),  # Combat Resistance (804A2EAF)
    (0x60, 2),  # Shot Resistance (804A2EB3)
    (0x6C, 2),  # Fire Resistance Level (804A2EBF)
    (0x70, 2),  # Water Resistance Level (804A2EC3)
    (0x74, 2),  # Thunder Resistance L... (804A2EC7)

    # EQUIPMENT/FM
    (0xB6, 77),  # Weapon Equipped Slo... (804A2F09)
    (0xB8, 3),  # Sub Weapon X (804A2F0B)
    (0xBA, 29),  # Sub Weapon Y (804A2F0D)
    (0xBC, 4),  # Erosion Slots (804A2F0F)
    (0xBD, 0),  # Is Force Metal 1 ON? (804A2F10)
    (0xBE, 72),  # Force Metal Slot 1 (804A2F11)
    (0xBF, 255),  # Is Force Metal 2 ON? (804A2F12)
    (0xC0, 255),  # Force Metal Slot 2 (804A2F13)
    (0xC1, 255),  # Is Force Metal 3 ON? (804A2F14)
    (0xC2, 255),  # Force Metal Slot 3 (804A2F15)
    (0xC3, 255),  # Is Force Metal 4 ON? (804A2F16)
    (0xC4, 255),  # Force Metal Slot 4 (804A2F17)

    # Hyper Mode
    (0xC8, 9),  # Current Erosion (804A2F1B)
    (0xCE, 2),  # Current Hyper Mode (804A2F21)
    (0xD0, 2)  # Max Hyper Mode (804A2F23)
]

# --- MASSIMO'S VANILLA PARAMETER DATA ---
MASSIMO_VANILLA_PARAMS = [
    # Level/ID
    (0x00, 11),  # Current Level
    (0x04, 3),

    # EXP
    (0x07, 10),  # # of 255's EXP
    (0x08, 80),  # EXP #

    # HP
    (0x0B, 6),   # # of 255's Current HP
    (0x0C, 251), # Current HP
    (0x0F, 6),   # # of 255's Max HP
    (0x10, 251), # Max HP
    (0x13, 6),   # # of 255's Actual HP
    (0x14, 251), # Actual HP

    # WE/Core Stats
    (0x18, 20), (0x1C, 25),
    (0x20, 59),  # Power Stat
    (0x24, 36),  # Armor Stat
    (0x28, 29),  # Shield Stat
    (0x2C, 37),  # Speed Stat
    (0x34, 100), (0x40, 1),

    # Resistances
    (0x5C, 2),
    (0x60, 2),
    (0x6C, 1),
    (0x70, 1),
    (0x74, 1),

    # EQUIPMENT/FM
    (0xB6, 100),   # Weapon Equipped
    (0xB7, 255),   # IS Sub Weapon 1 On?
    (0xB8, 255),   # Sub Weapon 1
    (0xB9, 255),   # IS Sub Weapon 2 On?
    (0xBA, 255),   # Sub Weapon 2
    (0xBC, 2),     # Erosion Slots
    (0xBD, 255),   # Is Force Metal 1 ON?
    (0xBE, 255),   # Force Metal 1
    (0xBF, 255),   # Is Force Metal 2 ON?
    (0xC0, 255),   # Force Metal 2
    (0xC1, 255),   # Is Force Metal 3 ON?
    (0xC2, 255),   # Force Metal 3
    (0xC3, 255),   # Is Force Metal #4 On?
    (0xC4, 255),   # Force Metal 4

    # Hyper Mode
    (0xC8, 13),    # Current Erosion
    (0xCE, 3),     # Current Hyper Mode
    (0xD0, 3),     # Max Hyper Mode
    # Action Trigger
    (0x354, 0)     # Massimo's Action Trigger
]

# --- MARINO'S VANILLA PARAMETER DATA ---
MARINO_VANILLA_PARAMS = [
    # Level/ID
    (0x00, 15),  # Marino's Level String (804A2FFB)
    (0x04, 4),  # Character Picture (ID) (804A2FFF)

    # EXP
    (0x07, 23),  # # of 255's EXP (804A3002)
    (0x08, 112),  # EXP # (804A3003)

    # HP
    (0x0B, 5),  # # of 255's Current HP (804A3006)
    (0x0C, 24),  # Current HP (804A3007)
    (0x0F, 5),  # # of 255's MAX HP (804A300A)
    (0x10, 24),  # Max HP (804A300B)
    (0x13, 5),  # # of 255's Actual HP (804A300E)
    (0x14, 24),  # Actual HP (804A300F)

    # WE/Core Stats
    (0x18, 32),  # Initial WE (804A3013)
    (0x1C, 25),  # WE Per Turn (804A3017)
    (0x20, 63),  # Power Stat (804A301B)
    (0x24, 42),  # Armor Stat (804A301F)
    (0x28, 41),  # Shield Stat (804A3023)
    (0x2C, 53),  # Speed Stat (804A3027)
    (0x34, 90),  # Accuracy (804A302F)
    (0x40, 5),  # Crit Chance (804A303B)

    # Resistances
    (0x5C, 2),  # Combat Resistance (804A3057)
    (0x60, 2),  # Shot Resistance (804A305B)
    (0x6C, 2),  # Fire Resistance (804A3067)
    (0x70, 2),  # Water Resistance (804A306B)
    (0x74, 2),  # Thunder Resistance (804A306F)

    # EQUIPMENT/FM
    (0xB6, 125),  # Marino's Weapon (804A30B1)
    (0xB8, 32),  # Sub Weapon X (804A30B3)
    (0xBA, 21),  # Sub Weapon Y (804A30B5)
    (0xBC, 3),  # Erosion Slots (804A30B7)
    (0xBD, 0),  # Is Force Metal #1 ON? (804A30B8)
    (0xBE, 37),  # Force Metal #1 (804A30B9)
    (0xBF, 255),  # Is Force Metal #2 ON? (804A30BA)
    (0xC0, 255),  # Force Metal #2 (804A30BB)
    (0xC1, 255),  # Is Force Metal #3 ON? (804A30BC)
    (0xC2, 255),  # Force Metal #3 (804A30BD)
    (0xC3, 255),  # Is Force Metal #4 ON? (804A30BE)
    (0xC4, 255),  # Force Metal #4 (804A30BF)
    (0xC7, 0),  # # of 255's Erosion (804A30C2)
    (0xC8, 18),  # Current Erosion (804A30C3)

    # Hyper Mode
    (0xCE, 5),  # Current Hyper Mode (804A30C9)
    (0xD0, 5),  # Max Hyper Mode (804A30CB)

    # ACTION TRIGGER
    (0x282, 1)  # Marino's Action Trigger Upgrade (804A327D)
]

# --- CINNAMON'S VANILLA PARAMETER DATA ---
CINNAMON_VANILLA_PARAMS = [
    # Level/ID
    (0x00, 1),  # Cinnamon's Level (804A30CF)
    (0x04, 5),  # Character Picture (ID) (804A30D3)

    # EXP
    (0x07, 0),  # # of 255's EXP (804A30D6)
    (0x08, 0),  # EXP # (804A30D7)

    # HP
    (0x0B, 1),  # # of 255's Current HP (804A30DA)
    (0x0C, 110),  # Current HP (804A30DB)
    (0x0F, 1),  # # of 255's MAX HP (804A30DE)
    (0x10, 110),  # Max HP (804A30DF)
    (0x13, 1),  # # of 255's Actual HP (804A30E2)
    (0x14, 110),  # Actual HP (804A30E3)

    # WE/Core Stats
    (0x18, 10),  # Initial WE (804A30E7)
    (0x1C, 25),  # WE Per Turn (804A30EB)
    (0x20, 9),  # Power Stat (804A30EF)
    (0x24, 17),  # Armor Stat (804A30F3)
    (0x28, 18),  # Shield Stat (804A30F7)
    (0x2C, 26),  # Speed Stat (804A30FB)
    (0x34, 100),  # Accuracy (804A3103)
    (0x40, 0),  # Crit Chance? (804A310F)

    # Resistances
    (0x5C, 2),  # Combat Resistance (804A312B)
    (0x60, 2),  # Shot Resistance (804A312F)
    (0x6C, 4),  # Fire Resistance (804A313B)
    (0x70, 4),  # Water Resistance (804A313F)
    (0x74, 4),  # Thunder Resistance (804A3143)

    # EQUIPMENT/FM
    (0xB6, 150),  # Cinnamon's Weapon (804A3185)
    (0xB8, 36),  # Sub Weapon X (804A3187)
    (0xB9, 255), # Sub Weapon Y OFF
    (0xBA, 255),  # Sub Weapon Y (804A3189)
    (0xBC, 3),  # Erosion Slots (804A318B)
    (0xBD, 255),  # Is Force Metal #1 On? (804A318C)
    (0xBE, 255),  # Force Metal #1 (804A318D)
    (0xBF, 255),  # Is Force Metal #2 On? (804A318E)
    (0xC0, 255),  # Force Metal #2 (804A318F)
    (0xC1, 255),  # Is Force Metal #3 On? (804A3190)
    (0xC2, 255),  # Force Metal #3 (804A3191)
    (0xC3, 255),  # Is Force Metal #4 On? (804A3192)
    (0xC4, 255),  # Force Metal #4 (804A3193)

    # Hyper Mode
    (0xC8, 20),  # Current Erosion (804A3197)
    (0xCE, 4),  # Current Hyper Mode (804A319D)
    (0xD0, 4),  # Max Hyper Mode (804A319F)

    # ACTION TRIGGER
    (0x1B0, 3)  # Cinnamon Action Trigger (804A327F)
]

# --- AXL'S VANILLA PARAMETER DATA ---
AXL_VANILLA_PARAMS = [
    # Level/ID
    (0x00, 17),  # Axl's Current Level (804A31A3)
    (0x04, 6),  # Character Picture (ID) (804A31A7)

    # EXP
    (0x07, 46),  # # of 255's EXP (804A31AA)
    (0x08, 224),  # EXP # (804A31AB)

    # HP
    (0x0B, 6),  # # of 255's Current HP (804A31AE)
    (0x0C, 91),  # Current HP (804A31AF)
    (0x0F, 6),  # # of 255's MAX HP (804A31B2)
    (0x10, 91),  # Max HP (804A31B3)
    (0x13, 6),  # # of 255's Actual HP (804A31B6)
    (0x14, 91),  # Actual HP (804A31B7)

    # WE/Core Stats
    (0x18, 25),  # Initial WE (804A31BB)
    (0x1C, 25),  # WE Gained Per Turn (804A31BF)
    (0x20, 68),  # Power Stat (804A31C3)
    (0x24, 43),  # Armor Stat (804A31C7)
    (0x28, 52),  # Shield Stat (804A31CB)
    (0x2C, 56),  # Speed Stat (804A31CF)
    (0x34, 98),  # Accuracy (804A31D7)
    (0x40, 2),  # Crit Chance (804A31E3)

    # Resistances
    (0x5C, 2),  # Combat Resistance (804A31FF)
    (0x60, 2),  # Shot Resistance (804A3203)
    (0x6C, 2),  # Fire Resistance (804A320F)
    (0x70, 2),  # Water Resistance (804A3213)
    (0x74, 2),  # Thunder Resistance (804A3217)

    # EQUIPMENT/FM
    (0xB6, 175),  # Axl's Weapon (804A3259)
    (0xB8, 7),  # Sub Weapon X (804A325B)
    (0xBA, 19),  # Sub Weapon Y (804A325D)
    (0xBC, 4),  # Erosion Slots (804A325F)
    (0xBD, 255),  # Is Force Metal #1 ON? (804A3260)
    (0xBE, 255),  # Force Metal #1 (804A3261)
    (0xBF, 255),  # Is Force Metal #2 ON? (804A3262)
    (0xC0, 255),  # Force Metal #2 (804A3263)
    (0xC1, 255),  # Is Force Metal #3 ON? (804A3264)
    (0xC2, 255),  # Force Metal #3 (804A3265)
    (0xC3, 255),  # Is Force Metal #4 ON? (804A3266)
    (0xC4, 255),  # Force Metal #4 (804A3267)

    # Hyper Mode
    (0xC8, 15),  # Current Erosion (804A326B)
    (0xCE, 2),  # Current Hyper Mode (804A3271)
    (0xD0, 2),  # Max Hyper Mode (804A3273)

    # ACTION TRIGGER
    (0xDE, 7)  # Axl Action Trigger (804A3281)
]

CHARACTER_DATA = {
    "X": {
        "params": X_VANILLA_PARAMS,
        "base_address": X_SLOT_BASE_ADDRESS,
    },
    "Zero": {
        "params": ZERO_VANILLA_PARAMS,
        "base_address": ZERO_SLOT_BASE_ADDRESS,
    },
    "Spider": {
        "params": SPIDER_VANILLA_PARAMS,
        "base_address": SPIDER_SLOT_BASE_ADDRESS
    },
    "Massimo": {
        "params": MASSIMO_VANILLA_PARAMS,
        "base_address": MASSIMO_SLOT_BASE_ADDRESS,
    },
    "Marino": {
        "params": MARINO_VANILLA_PARAMS,
        "base_address": MARINO_SLOT_BASE_ADDRESS,
    },
    "Cinnamon": {
        "params": CINNAMON_VANILLA_PARAMS,
        "base_address": CINNAMON_SLOT_BASE_ADDRESS,
    },
    "Axl": {
        "params": AXL_VANILLA_PARAMS,
        "base_address": AXL_SLOT_BASE_ADDRESS,
    },
}
