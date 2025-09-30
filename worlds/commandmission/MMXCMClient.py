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
        Serving as a place holder until we need custom commands!
        """
        logger.info("Mega Man X: Command Mission Client.")


async def mmxcm_update_non_savable_ram():
    value_to_write = bytes([1])
    memory_address = -0x804A20B1

    try:
        while True:
            dolphin.write_bytes(memory_address, value_to_write)
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

        if ctx.dolphin_server_task:
            await ctx.dolphin_server_task
    except Exception as genericEx:
        logger.error("Unable to run dolphin async. Ex: " + str(genericEx))


if __name__ == "__main__":
    # This ensures that the script will run the main function when executed.
    sync_main(*sys.argv[1:])