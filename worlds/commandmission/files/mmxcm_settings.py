import settings

class MMXCMIsoFile(settings.UserFilePath):
    """
    Locate the user's MMXCM PAL ISO file.
    """

    description = "MMXCM PAL ISO"
    copy_to = None


class MMXCMSettings(settings.Group):
    iso_file: MMXCMIsoFile = MMXCMIsoFile(MMXCMIsoFile.copy_to)