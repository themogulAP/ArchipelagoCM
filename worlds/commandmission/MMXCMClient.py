import asyncio
import sys

import Utils
from CommonClient import ClientCommandProcessor, get_base_parser, logger, server_loop, gui_enabled, CommonContext
import dolphin_memory_engine as dolphin

from .helpers import CLIENT_NAME


class MMXCMCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

    def _cmd_mmxcm(self, *args):
        """
        These are the commands for our MMXCM Client.
        Serving as a placeholder until we need custom commands!
        """
        logger.info("Mega Man X: Command Mission Client.")


async def mmxcm_update_non_savable_ram():
    SOFTLOCK_PREVENT_VALUE = bytes([1])
    SOFTLOCK_PREVENT_ADDRESS = 0x804A20B1

    ALWAYS_SUBTANK_ADDRESS = 0x804A329F
    ALWAYS_SUBTANK_VALUE = bytes([100])

    TANK_PARTS_PREVENT_ADDRESS = 0x804A329E
    TANK_PARTS_PREVENT_VALUE = bytes([0])

    ARAKURE_ADDRESS = 0x804A20A8
    ARAKURE_VALUE = bytes([33])

    CLEAR_PREONS_ADDRESS = 0x804A20BE
    CLEAR_PREONS_VALUE = 39

    # --- Testing RAM Writes: Full HP (255) for all health-related fields ---
    # WARNING: These are temporary and should be removed after the testing period.
    FULL_HP_VALUE = bytes([255])

    # SetsOfHPCurrent
    TEST_SETS_OF_HP_CURRENT_ADDRESS = 0x804A2CB6
    # HPCurrent
    TEST_HP_CURRENT_ADDRESS = 0x804A2CB7
    # SetsOfHPMax
    TEST_SETS_OF_HP_MAX_ADDRESS = 0x804A2CBA
    # HPMax
    TEST_HP_MAX_ADDRESS = 0x804A2CBB
    # SetsOfHPActual
    TEST_SETS_OF_HP_ACTUAL_ADDRESS = 0x804A2CBE
    # HPActual
    TEST_HP_ACTUAL_ADDRESS = 0x804A2CBF
    # ----------------------------------------------------------------------

    while not dolphin.is_hooked():
        await asyncio.sleep(1)

    try:
        while True:
            dolphin.write_bytes(SOFTLOCK_PREVENT_ADDRESS, SOFTLOCK_PREVENT_VALUE)
            dolphin.write_bytes(ALWAYS_SUBTANK_ADDRESS, ALWAYS_SUBTANK_VALUE)
            dolphin.write_bytes(TANK_PARTS_PREVENT_ADDRESS, TANK_PARTS_PREVENT_VALUE)
            dolphin.write_bytes(ARAKURE_ADDRESS, ARAKURE_VALUE)
            dolphin.write_bytes(CLEAR_PREONS_ADDRESS, CLEAR_PREONS_VALUE)

            # --- TESTING WRITES (Full HP) ---
            # Set all Current/Max/Actual HP values to 255 for invincibility testing
            dolphin.write_bytes(TEST_SETS_OF_HP_CURRENT_ADDRESS, FULL_HP_VALUE)
            dolphin.write_bytes(TEST_HP_CURRENT_ADDRESS, FULL_HP_VALUE)
            dolphin.write_bytes(TEST_SETS_OF_HP_MAX_ADDRESS, FULL_HP_VALUE)
            dolphin.write_bytes(TEST_HP_MAX_ADDRESS, FULL_HP_VALUE)
            dolphin.write_bytes(TEST_SETS_OF_HP_ACTUAL_ADDRESS, FULL_HP_VALUE)
            dolphin.write_bytes(TEST_HP_ACTUAL_ADDRESS, FULL_HP_VALUE)
            # --------------------------------

            # Add the small delay to prevent the loop.
            await asyncio.sleep(0.1)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        print("RAM write operation has stopped.")

def sync_main(*launch_args: str):
    Utils.init_logging(CLIENT_NAME)

    parser = get_base_parser()
    parser.add_argument('apmmxcm_file', default="", type=str, nargs="?", help='Path to an APMMXCM file')
    args = parser.parse_args(launch_args)

    if args.apmmxcm_file:
        from .MMXCMPatcher import MMXCMPatcher
        mmxcm_patch = MMXCMPatcher(args.apmmxcm_file)
        mmxcm_patch.create_patch()

    asyncio.run(async_main(args.connect, args.password))


async def async_main(connect, password):
    """
    This is the main function that will be called by the `CommonClient`
    to start our client.
    """

    try:
        # Create our context and initialize the command processor.
        from .MMXCMContext import MMXCMContext
        ctx = MMXCMContext(connect, password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")

        # Run the client!
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        ctx.dolphin_server_task = asyncio.create_task(ctx.dolphin_connect_loop(), name="MMXCM Dolphin Loop")
        ctx.mmxcm_nonsavable_ram_task = asyncio.create_task(mmxcm_update_non_savable_ram(), name="NonSavableRAMLoop")

        if ctx.dolphin_server_task:
            await ctx.dolphin_server_task
    except Exception as genericEx:
        logger.error("Unable to run dolphin async. Ex: " + str(genericEx))


if __name__ == "__main__":
    # This ensures that the script will run the main function when executed.
    sync_main(*sys.argv[1:])