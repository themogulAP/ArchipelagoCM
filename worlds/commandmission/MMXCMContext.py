from CommonClient import CommonContext

class MMXCMContext(CommonContext):
  """
  This is the context class for the Mega Man X: Command Mission client. 
  This will inherit from the core class "CommonContext" in AP.
  This will hold all the game information, state, and functionality to run the client.
  """
  def __init__(self, server_address: str = "", *args, **kwargs):
      super().__init__(server_address, *args, **kwargs)
    
      # We will use this list to store every location already checked.
      # This also makes sure to not send duplicates!
      self.checked_locations = set()

      # We will use this list to hold all items received in the multiworld.
      # This will be needed to give items to the player! 
      self.items_received = []

  def run_gui(self):
      """
      Placeholder for GUI, will be impleneted soon
      """
      pass
