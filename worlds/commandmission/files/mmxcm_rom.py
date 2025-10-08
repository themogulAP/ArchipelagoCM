import shutil

from worlds.Files import APPatch, APPlayerContainer, AutoPatchRegister
from settings import get_settings, Settings
from NetUtils import convert_to_base_types
import Utils

from hashlib import md5
from typing import Any
import json, logging, sys, os, zipfile, tempfile

logger = logging.getLogger()

RANDOMIZER_NAME = "Mega Man X Command Mission"

MMXCM_PAL_MD5 = 0xbd0f6597c620b7f7264d383e4e2531f8

class InvalidCleanISOError(Exception):
    """
    This exception will be raised when the user has an issue with their MMXCM Pal Rom.
    Message - - - the explanation of the error
    """

    def __init__(self, message="Invalid Clean ISO provided"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"InvalidCleanISOError: {self.message}"

class MMXCMPlayerContainer(APPlayerContainer):
    game = RANDOMIZER_NAME
    compression_method = zipfile.ZIP_DEFLATED
    patch_file_ending = ".apmmxcm"

    # Player options is the RANDOMIZED data based on the players options... not the options themselves.
    def __init__(self, player_options: dict, patch_path: str, player_name: str, player: int):
        self.output_data = player_options
        super().__init__(patch_path, player, player_name)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        opened_zipfile.writestr("patch.apmmxcm", json.dumps(self.output_data, indent=4, default=convert_to_base_types))
        super().write_contents(opened_zipfile)

class MMXCMPALPatch(APPatch, metaclass=AutoPatchRegister):
    game = RANDOMIZER_NAME
    hash = MMXCM_PAL_MD5
    patch_file_ending = ".apmmxcm"
    result_file_ending = ".iso"

    def __init__(self, *args: Any, **kwargs: Any):
        super(MMXCMPALPatch, self).__init__(*args, **kwargs)

    def __get_archive_name(self) -> str:
        if not (Utils.is_linux or Utils.is_windows):
            message = f"Your OS is not support with this Randomizer."
            logger.error(message)
            raise RuntimeError

        lib_path = ""
        if Utils.is_windows:
            lib_path = "lib-windows"
        elif Utils.is_linux:
            lib_path = "lib-linux"

        logger.info(f"Dependency archive name to use {lib_path}")
        return lib_path

    def __get_temp_folder_name(self) -> str:
        from ..helpers import CLIENT_VERSION
        temp_path = os.path.join(tempfile.gettempdir(), "commandmission", CLIENT_VERSION, "libs")
        return temp_path

    def patch(self, apmmxcm_patch:str):
        #Gets the AP path for base ROM.
        mmxcm_clean_iso = get_base_rom_path()
        logger.info("Provided MMXCM Iso Path was: " + mmxcm_clean_iso)

        base_path = os.path.splitext(apmmxcm_patch)[0]
        output_file = base_path + self.result_file_ending

        try:
            # Make sure we have the clean rom first
            self.verify_base_rom(mmxcm_clean_iso, throw_on_missing_speedups=True)

            # Calls the MMXCMPatcher to patch the file into ISO
            from ..MMXCMPatcher import MMXCMPatcher
            MMXCMPatcher(apmmxcm_patch)
        except ImportError:
            self.__get_remote_dependencies_and_create_iso(apmmxcm_patch, mmxcm_clean_iso)
        return output_file

    def read_contents(self, apmmxcm_patch: str) -> dict[str, Any]:
        with zipfile.ZipFile(apmmxcm_patch, "r") as zf:
            with zf.open("archipelago.json", "r") as f:
                mainfest = json.load(f)

        if mainfest["compatible_version"] > self.version:
            raise Exception(f"File (version: {mainfest['compatible_version']}) too new"
                            f"for this handler (version: {self.version}")
        return mainfest

    @classmethod
    def verify_base_rom(cls, mmxcm_rom_path: str, throw_on_missing_speedups: bool = False):
        # Double checks that we have a valid PAL installation of MMX CM.
        logger.info("Verifying if ISO is Mega Man X Command Mission PAL.")
        logger.info("Checking gclib and speedups.")
        # Making sure speedups is available
        import pyfastyaz0yay0
        from gclib import fs_helpers as fs, yaz0_yay0
        logger.info("Using GClib from path: %s.", fs.__file__)
        logger.info("Using speedups from path: %s.", pyfastyaz0yay0.__file__)
        logger.info(sys.modules["gclib.yaz0_yay0"])

        if yaz0_yay0.PY_FAST_YAZ0_YAY0_INSTALLED:
            logger.info("Speedups detected.")
        else:
            logger.info("Python module paths: %s", sys.path)
            if throw_on_missing_speedups:
                logger.info("Speedups not detected, attempting to pull remote release.")
                raise ImportError("Cannot continue patching MMX CM due to missing libraries")
            logger.info("Continuing patching without speedups.")

        base_md5 = md5()
        with open(mmxcm_rom_path, "rb") as f:
            while chunk := f.read(1024 * 1024): # - - -This reads the file in 1 MB chunks.
                base_md5.update(chunk)

            # This grabs the Game ID and the Code while the file is open.
            code = fs.try_read_str(f,0,4)
            game_id = fs.try_read_str(f,0,6)
            logger.info(f"Code: {code}")
            logger.info(f"MMXCM Game ID: {game_id}")

        # Double checks the file is correct first.
        md5_conv = int(base_md5.hexdigest(), 16)
        if md5_conv != MMXCM_PAL_MD5:
            raise InvalidCleanISOError(f"Invalid Vanilla {RANDOMIZER_NAME} ISO... Check it is not corrupted!")

        #Double check the file has a correct iso format file extension
        if code == "CISO":
            raise InvalidCleanISOError(f"Invalid vanilla {RANDOMIZER_NAME} ISO... make sure it is .ISO")

        else:
            raise InvalidCleanISOError("Invalid game given as vanilla MMXCM Iso. Verify it is the Vanilla PAL iso!")

    def create_iso(self, temp_dir_path: str, patch_file_path: str, vanilla_iso_path: str):
        logger.info(f"Appending the following to sys path to get dependencies: {temp_dir_path}")
        sys.path.insert(0, temp_dir_path)

        # Verify it's the clean rom.
        self.verify_base_rom(vanilla_iso_path)

        #Use the Patcher to patch it into an iso.
        from ..MMXCMPatcher import MMXCMPatcher
        MMXCMPatcher(patch_file_path)

    def __get_remote_dependencies_and_create_iso(self, apmmxcm_patch: str, mmxcm_clean_iso: str):
        local_dir_path = self.__get_temp_folder_name()
        try:
            # Remove the temporary directory if we failed to patch the ISO correctly.
            if os.path.isdir(local_dir_path):
                logger.info("Found temp directory after failing seed generation, deleting %s.", local_dir_path)
                shutil.rmtree(local_dir_path)
                os.makedirs(local_dir_path, exist_ok=True)

                #Load external dependencies based on which OS
                logger.info("Temporary Directory created as: %s", local_dir_path)
                self.create_iso(local_dir_path, apmmxcm_patch, mmxcm_clean_iso)
        except PermissionError:
            logger.warning("Failed to cleanup temp folder, %s ignoring delete.", local_dir_path)

def get_base_rom_path() -> str:
    options: Settings = get_settings()
    file_name = (options.get("commandmission_options", "")).get("iso_file", "")
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name


