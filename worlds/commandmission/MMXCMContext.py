from CommonClient import CommonContext
from NetUtils import NetworkItem
from typing import Dict
import dolphin_memory_engine as dolphin

from worlds.commandmission.helpers import CONNECTION_LOST_STATUS


class MMXCMContext(CommonContext):
  """
  This is the context class for the Mega Man X: Command Mission client. 
  This will inherit from the core class "CommonContext" in AP.
  This will hold all the game information, state, and functionality to run the client.
  """

  async def disconnect(self, allow_autoreconnect: bool = False):
      """
      Disconnect the client from the server and reset game state variables.

      :param allow_autoreconnect: Allow the client to auto-reconnect to the server. Defaults to `False`.

      """
      await super().disconnect(allow_autoreconnect)
      self.auth = None
      dolphin.un_hook()
      self.dolphin_status = CONNECTION_LOST_STATUS
      self.already_fired_events = False

  item_id_to_name: Dict[int, str]

  slot_to_player_name: Dict[int,str]

  def __init__(self, server_address: str = "", settings: dict = None, *args, **kwargs):
      super().__init__(server_address, *args, **kwargs)
    
      # We will use this list to store every location already checked.
      # This also makes sure to not send duplicates!
      self.checked_locations = set()

      # We will use this list to hold all items received in the multiworld.
      # This will be needed to give items to the player! 
      self.items_received = []

      #This also stores our options from MMXCMOptions, which is determined by player.
      self.settings = settings

  def run_gui(self):
      """
      Placeholder for GUI, will be implemented soon.
      Not needed for basic interface of usual APs? 
      """
      pass

  async def on_package(self, cmd: str , args: dict): 
    """
    This is the method that is called by CommonClient when a package is received from the server.
    """

    # This will check if the client is correctly connected to the AP server
    if cmd == "Connected":
        self.game_running = True
        await self.send_connect()
        print("Successfully connected to the Archipelago server!")

    # This checks if the incoming message from AP server is "Received Items"
    elif cmd == "ReceivedItems":
      # This is the package sent when we get something from a different player.
      items_to_add = []
      for item in args["items"]:
          # This is the format of the item.
          items_to_add.append(NetworkItem(*item))

      # This will check the list of items to give to player before continuing. 
      if items_to_add:
          self.items_received.extend(items_to_add)
          print(f"Received {len(items_to_add)} new item(s) from the MultiWorld.")
          for item in items_to_add:
              print(f" - {self.item_id_to_name.get(item.item, 'Unknown Item')} from {self.player_names[item.player]}")

      # Prints messages from the Server, like hints! 
    elif cmd == "Print":
          print(args["text"])
            
