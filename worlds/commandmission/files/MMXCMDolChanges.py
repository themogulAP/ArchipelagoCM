# This is our section that will iilustrate the direct code changes we need to make... before any randomization.
# If adding more changes: fill in this dictionary with the address and new bytes.
CODE_PATCHES = [
    {
        # -----------------------Prevent Party Members From Leaving ------------------------
        # Party Member Slot Strings
        # Original RAM Address: 800d7E0C
        "address": 0x0D4E0C,
        "data": [0x60, 0x00, 0x00, 0x00]  # NOP Instruction
    },
    {
        # Of Party Members
        # Original Ram: 800d7e2c
        "address": 0x0D4E2C,
        "data": [0x38, 0x06, 0x00, 0x00]  # Sets the character substraction to 0.
    },
        # -----------------------------GAME BOOT SEQUENCE FLAGS----------------------
    {
        # Loading into Arcade: Scenario Flag
        # RAM Address: 800Dbab4
        "address": 0x0AAB4,
        "data": [0x38, 0x60, 0x00, 0x0A]
    },
    {
        # Loading into Arcade: Stage #
        # RAM: 80011d04
        "address": 0x0ED04,
        "data": [0x3C, 0x60, 0x00, 0x02]
    },
    {
        # Loading into arcade: Area # and Spawn Letter
        # RAM: 80011d08
        "address": 0x0ED08,
        "data": [0x38, 0x03, 0x05, 0x4C]
    },
    {
        # Set Flag Chpt 10 Cutscene
        # RAM: 8000d8f8
        "address": 0x0A8F8,
        "data": [0x38, 0x60, 0x00, 0x02]
    },
    {
        # Store Chpt 10 Cutscene
        # RAM: 8000d8fc
        "address": 0x0A8FC,
        "data": [0x98, 0x64, 0x00, 0x48]
    },
        # ------------------------- CHAPTER 2 SPECIFIC CHANGES -----------------------------
    {
        # Sets PREON BIT in Data Backup Room B AND A to Despawn... prevents walking bug.
        # RAM: 8000D900
        "address": 0x0A900,
        "data": [0x38, 0x60, 0x00, 0x07]
    },
    {
        # STORES PREON BIT in Data Backup Room B AND A to Despawn... prevents walking bug.
        # RAM: 8000D900
        "address": 0x0A904,
        "data": [0x98, 0x64, 0x00, 0x54]
    },
    {
        # Sets cutscenes Intruders and Spider Fight
        # RAM: 8000d908
        "address": 0x0A908,
        "data": [0x38, 0x60, 0x00, 0xC0]
    },
    {
        # Stores BYTE FOR cutscene for Intruders + Spider Fight
        # RAM: 8000d90c
        "address": 0x0A90C,
        "data": [0x98, 0x64, 0x00, 0x5D] # 98 = Store BYTE in PPC.
    },
    {
        # Sets the Preon Battle 2E in Command Room to Finished -
        # RAM: 8000d910
        "address": 0x0A910,
        "data": [0x38, 0x60, 0x00, 0x04]
    },
    {
        # STORE the Preon Battle 2E in Command Room to Finished -
        # RAM: 8000d914
        "address": 0x0A914,
        "data": [0x98, 0x64, 0x00, 0x62]
    },
    {
        # Sets BYTE FOR Arcade, Jango's, and Bed Door
        # RAM: 8000d919
        "address": 0x0A918,
        "data": [0x38, 0x60, 0x00, 0x19]
    },
    {
        # Stores BYTE FOR Arcade, Jango's, and Bed Door
        # RAM: 8000d91C
        "address": 0x0A91C,
        "data": [0x98, 0x64, 0x00, 0x63]
    },
    {
        # sets every other flag back to zero
        # RAM: 8000d920
        "address": 0x0A920,
        "data": [0x38, 0x60, 0x00, 0x00]
    },
    {
        # Stores every other flag to zero
        # RAM: 8000d92C
        "address": 0x0A924,
        "data": [0x90, 0x64, 0x00, 0x74]
    },
    {
        # -----------------------------SOFT LOCK PREVENT IN CHAPTER 2-----------------------------
        # Prevents the NPC from being removed after battle or entering the room.
        # RAM Address: 80039cd4
        "address": 0x036CD4,
        "data": [0x38, 0x60, 0x00, 0x01]
    },
        # --------------------------- PREVENT BEATING THE GAME ----------------------
    {
        # Prevent beating the Game --- Change comparison
        # RAM Address: 8001047c
        "address": 0x0D47C,
        "data": [0x2c, 0x04, 0x00, 0x3D]
    },
    {
        # Change the equation to add zero to scenario flag
        # RAM: 800104c4
        "address": 0x0D4C4,
        "data": [0x38, 0x03, 0x00, 0x00]
    },
    {
        # Set Every Previous Chapter Flag to Unclear
        # RAM: 800104e8
        "address": 0x0D4E8,
        "data": [0x60, 0x00, 0x00, 0x00]
    },
        # --------------------- ALL TELEPORT PREVENTION UNTIL ACCESS CODES ----------------------------------------
    {
        # Change Lagrano Ruins to teleport back to Central Tower STAGE w/o Access Code
        # RAM Address Label: 80082fac
        "address": 0x07ffa4,
        "data": [0x3c, 0x80, 0x00, 0x02]
    },
    {
        # Change Lagrano Ruins AREA back to Shopping Arcade w/o Access Code
        # RAM: 80082fac
        "address": 0x07ffac,
        "data": [0x38, 0x04, 0x05, 0x4F]
    },
    {
        # Change Tianna Camp Stage to Central Tower w/o Access Code
        # RAM Address: 80082fcc
        "address": 0x07ffcc,
        "data": [0x3c, 0x80, 0x00, 0x02]
    },
    {
        # Change Tianna Camp AREA to Central Tower...
        # RAM: 80082fd4
        "address": 0x07ffd4,
        "data": [0x38, 0x04, 0x05, 0x4F]
    },
    {
        # Changes Gaudile Laboratory back to Central Tower
        # RAM: 80082ff4
        "address": 0x07fff4,
        "data": [0x3c, 0x80, 0x00, 0x02]
    },
    {
        # Changes Gaudile Laboratory back to Shopping Arcade
        # RAM: 80082ffc
        "address": 0x07fffc,
        "data": [0x38, 0x04, 0x05, 0x4F]
    },
    {
        # Changes Ulfat Factory to Central Tower teleport
        # RAM Address: 8008301c
        "address": 0x08001c,
        "data": [0x3c, 0x80, 0x00, 0x02]
    },
    {
        # Changes Ulfat Factory AREA to Shopping Arcade
        # RAM: 80083204
        "address": 0x080024,
        "data": [0x38, 0x04, 0x05, 0x4F]
    },
    {
        # Changes Gimialla Mine to Central Tower stage
        # RAM Address: 80083044
        "address": 0x080044,
        "data": [0x3c, 0x80, 0x00, 0x02]
    },
    {
        # Changes Gimialla Mine AREA to Shopping Arcade
        # RAM: 8008304c
        "address": 0x08004c,
        "data": [0x38, 0x04, 0x05, 0x4F]
    },
    {
        # Changes Melda Ore Plant to Central Tower Stage
        # RAM: 80083094
        "address": 0x080094,
        "data": [0x3c, 0x80, 0x00, 0x02]
    },
    {
        # Changes Melda Ore Plant AREA to Shopping Arcade
        # RAM: 8008309c
        "address": 0x08009c,
        "data": [0x38, 0x04, 0x05, 0x4F]
    },
    {
        # Changes Grave Ruins Base to Central Tower Stage
        # RAM: 800830bc
        "address": 0x0800BC,
        "data": [0x3c, 0x80, 0x00, 0x02]
    },
    {
        # Changes Grave Ruins Base AREA to Shopping Arcade
        # RAM: 800830c4
        "address": 0x0800c4,
        "data": [0x38, 0x04, 0x05, 0x4F]
    },
    {
        # Switches "Back to Hunter Base" teleport to Arcade from Save Spots.
        # RAM: 8001cc08
        "address": 0x019C08,
        "data": [0x60, 0x84, 0x05, 0x4C]
    },
        # ------------------------------ITEM INVENTORY FIXES ----------------------------------------
    {
        # NOP the Writing item to inventory BASE GAME code.
        # RAM: 800d7360
        "address": 0x0D4360,
        "data": [0x60, 0x00, 0x00, 0x00]
    },
    {
        # NOP the Writing QUANTITY to inventory BASE GAME code.
        # RAM: 800d7364
        "address": 0x0D4364,
        "data": [0x60, 0x00, 0x00, 0x00]
    },
        # -----------------------------FORCE METAL TURNED ON FIX -----------------------------------
    {
        # Ori the values we need for Setting the preon and battle to off in Lagrano + the Door Open.
        # RAM: 8000d8ec
        "address": 0x0A8EC,
        "data": [0x60, 0x63, 0x40, 0x81]
    },
    {
        # SETS the the preon and battle to off in Lagrano + the Door Open.
        # RAM: 8000d8f0
        "address": 0x0A8F0,
        "data": [0x90, 0x64, 0x00, 0x33]
    },
    {
        # NOP the following so we can load into the Next set of code patches.
        # RAM: 8000d8f4
        "address": 0x0A8F4,
        "data": [0x60, 0x00, 0x00, 0x00]
    },
        # ----------------------- Sub Tank Control Patches ----------------------------
    {
        # Set Sub Tank fill amount to a constant 100 (0x64).
        # Original RAM Address: 80110f70
        "address": 0x10DF70,
        "data": [0x38, 0xe0, 0x00, 0x64]  # li r7, 100 (0x64)
    },
    {
        # Store the constant Sub Tank fill amount (r7) into the Sub Tank % slot.
        # Original RAM Address: 80110f80
        "address": 0x10DF80,
        "data": [0x98, 0xe9, 0x12, 0x3F]  # stb r7, 0x123F(r9)
    },
    {
        # Prevents adding Sub Tank % from a specific event/location (Original: sth r0, 0x123E(r4)).
        # Original RAM Address: 800d6e6c
        "address": 0x0D3E6C,
        "data": [0x60, 0x00, 0x00, 0x00]  # NOP
    },
    {
        # Change Sub Tank loss calculation to set r3 to 100 (instead of subtracting), preventing loss.
        # Original RAM Address: 800abbc8
        "address": 0x0A8BC8,
        "data": [0x38, 0x60, 0x00, 0x64]  # li r3, 100 (0x64)
    },
    {
        # Prevents Sub Tank % gain from the Bed (Original: sth r0, 0x123E(r4)).
        # Original RAM Address: 800d359c
        "address": 0x0D059C,
        "data": [0x60, 0x00, 0x00, 0x00]  # NOP
    },
    {
        # Prevents Sub Tank % gain on a random one in Lagrano (Original: sth r5, 0x123E(r4)).
        # Original RAM Address: 800d6e7c
        "address": 0x0D3E7C,
        "data": [0x60, 0x00, 0x00, 0x00]  # NOP
    },
    {
        # Change Sub Tank add limit from 'addi r0, r3, 100' to 'addi r0, r3, 0', preventing limit add on more tank parts.
        # Original RAM Address: 800d6fac
        "address": 0x0D3FAC,
        "data": [0x38, 0x03, 0x00, 0x00]  # addi r0, r3, 0
    },
]