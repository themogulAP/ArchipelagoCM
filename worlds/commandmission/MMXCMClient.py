import asyncio
import sys
from typing import TYPE_CHECKING

import Utils
from CommonClient import ClientCommandProcessor, get_base_parser, logger, server_loop, gui_enabled, CommonContext

from .helpers import CLIENT_NAME

if TYPE_CHECKING:
    from .MMXCMContext import MMXCMContext


class MMXCMCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: "MMXCMContext"):
        super().__init__(ctx)

    def _cmd_mmxcm(self, *args):
        """
        These are the commands for our MMXCM Client.
        Serving as a placeholder until we need custom commands!
        """
        logger.info("Mega Man X: Command Mission Client.")

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
        ctx.mmxcm_nonsavable_ram_task = asyncio.create_task(ctx.mmxcm_update_non_savable_ram(), name="NonSavableRAMLoop")

        await ctx.exit_event.wait()
        await ctx.shutdown()

        if ctx.dolphin_server_task:
            await ctx.dolphin_server_task

        if ctx.mmxcm_nonsavable_ram_task:
            await ctx.mmxcm_nonsavable_ram_task
    except Exception as genericEx:
        logger.error("Unable to run dolphin async. Ex: " + str(genericEx))


if __name__ == "__main__":
    # This ensures that the script will run the main function when executed.
    sync_main(*sys.argv[1:])