import asyncio
from typing import NamedTuple, Optional

""" Collection of commonly used constants for MMX Command Mission. """

CLIENT_VERSION = "V0.1.0"
CLIENT_NAME = "Mega Man X Command Mission Client"

AP_LOGGER_NAME = "Client"
AP_WORLD_VERSION_NAME = "APWorldVersion"

# All the dolphin connection messages used in the client
CONNECTION_REFUSED_STATUS = "Detected a non-randomized ROM for MMXCM. Please close and load a different one. Retrying in 5 seconds..."
CONNECTION_LOST_STATUS = "Dolphin connection was lost. Please restart your emulator and make sure MMXCM is running."
NO_SLOT_NAME_STATUS = "No slot name was detected. Ensure a randomized ROM is loaded. Retrying in 5 seconds..."
CONNECTION_VERIFY_SERVER = "Dolphin was confirmed to be opened and ready, Connect to the server when ready..."
CONNECTION_INITIAL_STATUS = "Dolphin emulator was not detected to be running. Retrying in 5 seconds..."
CONNECTION_CONNECTED_STATUS = "Dolphin is connected, AP is connected, have fun on your MMXCM playthrough!"

class StringByteFunction:
    @staticmethod
    def string_to_bytes(user_string: str, encoded_byte_length: int) -> bytes:
        """
        Encodes a provided string to UTF-8 format. Adds padding until the expected length is reached.
        If provided string is longer than expected length, raise an exception

        :param user_string: String that needs to be encoded to bytes.
        :param encoded_byte_length: Expected length of the provided string.
        """
        encoded_string = user_string.encode('utf-8')

        if len(encoded_string) < encoded_byte_length:
            encoded_string += b'\x00' * (encoded_byte_length - len(encoded_string))
        elif len(encoded_string) > encoded_byte_length:
            raise Exception("Provided string '" + user_string + "' was longer than the expected byte length of '" +
                            str(encoded_byte_length) + "', which will not be accepted by the info file.")

        return encoded_string

class MMXCMRamData(NamedTuple):
    ram_addr: Optional[int] = None
    bit_position: Optional[int] = None
    ram_byte_size: Optional[int] = None
    pointer_offset: Optional[int] = None
    item_count: Optional[int] = None

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

async def wait_for_next_loop(time_to_wait: float):
    await asyncio.sleep(time_to_wait)
