# Mega Man X Command Mission Multiworld Setup Guide

## Required Software

- [Archipelago Multiworld Suite](https://github.com/ArchipelagoMW/Archipelago/releases). 
- [Dolphin Gamecube/Wii Emulator](https://dolphin-emu.org/)
- Your EU ISO file, probably named `Mega Man X - Command Mission (Europe).iso`. Support for the US version is planned in the distant future.
- The GClib (extracted) folder from the lib-windows or lib-linux in the releases page.
- The latest Commandmission AP world (from releases page). 

## Installation Procedures

1. Download and install the Archipelago Multiworld Suite from the link above, making sure to install the most recent version.

2. Acquire the most recent APWorld from the [Releases Page](https://github.com/themogulAP/ArchipelagoCM/releases) and place the commandmission.apworld in the custom_worlds folder of your Archipelago install.

3. Acquire the lib-windows (if you are on Windows) OR lib-linux if you are on Linux.

4. Place this lib folder into your Archipelago installation folder. Navigate to the /lib folder in this Archipelago installation, and "Export Here".

5. This should place a folder named "gclib" into the /lib of the Archipelago installation on your device. 

6. Download and install the Dolphin Gamecube/Wii Emulator from the link above, making sure to install the most recent version.
Run the emulator at least once to make sure it is working.

7. Make sure Dolphin's MMU (Memory Management Unit) is disabled / un-checked. This is found under the Options Menu in Dolphin > Configuration > Advanced tab. 

8. Note for Mac users: Due to additional security hardening that Apple added to MacOS, the steps from [here](https://github.com/aldelaro5/dolphin-memory-engine?tab=readme-ov-file#macos-code-signing) relating to Code Signing must be performed. Not doing so will prevent your Archipelago Client from connecting to the game appropriately.

## Main Troubleshooting:
1. If the dialog window is not prompting for a .iso file after pressing "Open Patch":
-- Double check your host.yaml settings in your archipelago installation. 

Your host.yaml should say something like this for 
commandmission_options:
   Locate the user's MMXCM PAL ISO file.
  iso_file: "C:/Users/.../PAL ISO/Mega Man X - Command Mission (Europe) (En,Fr,De).iso"

NOTE: These need to be the / (backslash), not the forward slash! You may have to manually put in your ROM path if the window does not populate. 
Further questions on this, please respond in the Archipelago channel with your attached logs (also in the Archipelago installation). 

2. Any other issues, please refer to your Archipelago attached logs. These will be absolutely imperative to fixing any problems that may arise.
A common example is when your log says "NoneType"....

If it says this "NoneType" error... please double check your rom that is a .iso ONLY! You cannot convert into .iso from other file formats. 

## Create a Config (.yaml) File

### What is a config file and why do I need one?

Your config file contains a set of configuration options which provide the generator with information about how it
should generate your game. Each player of a multiworld will provide their own config file. This setup allows each player
to enjoy an experience customized for their taste, and different players in the same multiworld can all have different
options.

### Where do I get a config file?

Run the ArchipelagoLauncher.exe from your Archipelago install and click `Generate Template Options`.
This will produce a `/Players/Templates` folder in your Archipelago install, which contains default config files for 
every game in your `custom_worlds` and `lib/worlds` folder. You can manually edit the config file using a text editor of your choice.

Alternately, the [Player Settings](../player-settings) page on the website allows you to configure
your personal settings and export a config file from them.

### Verifying your config file

If you would like to validate your config file to make sure it works, you may do so on the
[YAML Validator](/mysterycheck) page.

## Generating a Single-Player Game

1. After modifying your yaml, place it into your Archipelago/player folder
   - Alternately, navigate to the [Player Settings](../player-settings) page, configure your options,
      and click the "Generate Game" button.
2. Open the Archipelago Launcher and click "Generate". This will create a zip file in Archipelago/output
   - You will need to open this .zip to get your .apmmxcm patch file if you are not using the Archipelago website.
3. Navigate to the Archipelago website and go to the Host Game page (top right menu)
4. Click upload file and pass it the .zip created in your output folder
5. Click the "Create New Room" link. You are now able to download your patch file from here (as of AP 0.6.2).
6. Run the ArchipelagoLauncher.exe and click `Open Patch`. Select your `.apmmxcm` patch file.
You will be prompted to locate your Mega Man X Command Mission (PAL) ISO the first time you do this.
   - This action will AUTOMATICALLY run the MMXCM Client (and connect to the webhost if the patch was downloaded from there).
   - The patch will be placed in the same folder as your patch file by default.
   - You will ***not*** need to patch the game every time, and can simply run the `MMXCMClient` from the list on the right of the Archipelago Launcher
to continue later.
7. Open Dolphin and from Dolphin, open your newly patched Mega Man X Command Mission ISO. Load all the way into a brand new save file, and pause.
   - Ensure that "Enable GPU Overclock" and "Emulated Memory Size Override" are both off in your Dolphin settings
   - You ***must*** use a brand new save file, not a New Game Plus file
8. In the server page, there will be a port number. Copy this port number into the top of your MMXCMClient if it did not populate on its own. 
   - The field should read `archipelago.gg:<port number>`
9. Once you have loaded into the game, click the `Connect` button at the top of the MMXCMClient. You are now connected and ready to play!
10. NOTE: You MUST open the Client and connect to the AP Server FIRST, before opening Dolphin emulator and the patched rom!

## Joining a MultiWorld Game

### Obtain your patch file and create your ROM

When you join a multiworld game, you will be asked to provide your config file to whoever is hosting. Once that is done,
the host will provide you with either a link to download your patch file, or with an APMMXCM patch file that they have extracted from the zip. 

Put your patch file on your desktop or somewhere convenient. Open the ArchipelagoLauncher.exe and click `Open Patch`. 
This should automatically launch the client, and will also create your ISO in the same place as your patch file. On first time patching, you will be prompted 
to locate your Mega Man X Command Mission PAL ISO. 
Note: The first time patching your PAL ISO rom may take a few minutes! 

### Connect to the client

When the ISO patched, the Mega Man X Command Mission client (MMXCMClient) should have also automatically launched in
the background. If it did not, please check the log in your Archipelaog/logs folder. If this is its first time launching, you may be prompted to allow it to communicate through the Windows Firewall. You must reopen the client each time you connect to a different randomized ISO.

1. Open Dolphin and from Dolphin, open your newly patched Mega Man X Command Mission ISO
2. In the server page, there will be a port number. Copy this port number into the top of your MMXCMClient. 
   - The field should read `archipelago.gg:<port number>`
3. Once you have loaded into the game, the client should log that Dolphin has been connected. Click the `Connect` button
at the top of the MMXCMClient. If the port number is correct, you are now connected and ready to play!
NOTE: You MUST open the Client and connect to the AP Server FIRST, before opening Dolphin emulator and the patched rom!

### Play the game
### Enjoy your MMXCM Playthrough!
