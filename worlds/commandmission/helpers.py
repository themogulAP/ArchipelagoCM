from typing import NamedTuple, Optional, Any
from worlds.Files import APPatch, APPlayerContainer, AutoPatchRegister
from NetUtils import convert_to_base_types
from hashlib import md5
import Utils

from settings import get_settings, Settings
import json, logging, os, sys, zipfile, tempfile

from .MMXCMPatcher import MMXCMPatcher

logger = logging.getLogger()
RANDOMIZER_NAME = "Mega Man X Command Mission"

MMXCM_PAL_MD5 = 0xBD0F6597C620B7F7264D383E4E2531F8

# This is the main class that the Archipelago Launcher interacts with.
class MMXCMPatchFile(APPatch, metaclass=AutoPatchRegister):
    # These attributes are required by the framework.
    game = "Mega Man X: Command Mission"
    hash = MMXCM_PAL_MD5
    patch_file_ending = ".apmmxcm"
    result_file_ending = ".iso"
    procedure = ["custom"]

    @classmethod
    def get_base_rom_path(cls) -> str:
        # This method is also required by the framework. It finds the game's ROM in the user's settings.
        options: Settings = get_settings()
        file_name = options["mmxcm_options"]["iso_file"]
        if not os.path.exists(file_name):
            file_name = Utils.user_path(file_name)
        return file_name

    @classmethod
    def verify_base_rom(cls, mmxcm_rom_path: str, throw_on_missing_speedups: bool = False):
        # This method verifies the user's game file.
        logger.info("Verifying if the provided ISO is a valid copy of Mega Man X: Command Mission PAL edition.")
        base_md5 = md5()
        with open(mmxcm_rom_path, "rb") as f:
            while chunk := f.read(1024 * 1024):
                base_md5.update(chunk)
            
            f.seek(0x01)
            game_id = f.read(5).decode('utf-8')
            logger.info(f"MMXCM Game ID: {game_id}")
            if game_id != "GMXP52":
                logger.warning("Game ID does not match expected PAL version. Continuing anyway.")
        
        md5_conv = int(base_md5.hexdigest(), 16)
        if md5_conv != MMXCM_PAL_MD5:
            logger.warning(f"Invalid vanilla {MMXCMPatchFile.game} ISO. The MD5 hashes do not match. Continuing anyway.")

    def patch(self, ap_patch_path: str) -> str:
        """
        This is the main method that runs when the user patches the game.
        """
        # 1. Get the path to the clean ISO from the user's settings.
        mmxcm_clean_iso = self.get_base_rom_path()
        
        # 2. Define the path for the new randomized ISO.
        base_path = os.path.splitext(ap_patch_path)[0]
        output_file = base_path + self.result_file_ending

        # 3. Read the randomization data from the seed file.
        with zipfile.ZipFile(ap_patch_path, "r") as zf:
            ap_output_data = zf.read("patch.apmmxcm")
            
        randomization_data = json.loads(ap_output_data.decode('utf-8'))
        
        # 4. Instantiate the core patcher and create the patch.
        # This is where our code calls the clean, self-contained patcher class.
        core_patcher = MMXCMPatcher(mmxcm_clean_iso, output_file)
        core_patcher.create_patch(randomization_data, "", "") # base_path and destination_path are not used by MMXCMPatcher

        return output_file

# A class for if the iso is not correct. 
class InvalidCleanISOError(Exception):
    """
    Exception raised for when user has an issue with their provided MMX Command Mission ISO.

    Attributes:
        message -- Explanation of the error
    """

    def __init__(self, message="Invalid Clean ISO provided"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"InvalidCleanISOError: {self.message}"

# This Player Container tells AP "hey we need an output file here". 
class MMXCMPlayerContainer(APPlayerContainer):
    game = RANDOMIZER_NAME
    compression_method = zipfile.ZIP_DEFLATED
    patch_file_ending = ".apmmxcm"

    def __init__(self, player_choices: dict, output_file_path: str, player_name: str, player: int,
        server: str = ""):
        self.output_data = player_choices
        super().__init__(output_file_path, player, player_name, server)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        opened_zipfile.writestr("patch.apmmxcm", json.dumps(self.output_data, indent=4, default=convert_to_base_types))
        super().write_contents(opened_zipfile)

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
