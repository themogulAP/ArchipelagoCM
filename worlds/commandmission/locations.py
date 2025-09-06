from tpying import NamedTuple, Dict, Optional
from .Items import MMXCMItemData
from .Helpers import MMXCMRamData

# This will list the exact bluepring for makign our locations! 
class MMXCMLocationData(NamedTuple):
  name:str
  code:Optional[int]
  parent_region: str
  ram_addr: Optional[MMXCMRamData] = None

# This begins the list for every single randomized item in AP.
LAGRANO_RUINS_LOCATIONS: dict[str, MMXCMLocationData] = {
  # Here is an example of the location and the bit position to track it.
  "Area 1F East 50z"
