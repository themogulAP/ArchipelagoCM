# This file is where every setting is defined that the player can choose, thus defining logic.
from dataclasses import dataclass
from Options import Toggle, Range, Choice, DeathLink, OptionDict, NamedRange, PerGameCommonOptions

# Setting the # of Rebellion Medals the player needs to access Chapter 10.
class rebellion_medal_count(Range):
  display_name = "Rebellion Medal Count"
  internal_name = "rebellion_medal_count"
  default=9
  range_start=0
  range_end=9

#This is the Option choice for the player's desired encounter rate.
class encounter_rate(Choice):
  display_name = "Encounter Rate"
  internal_name = "encounter_rate"
  option_off = 0
  option_vanilla = 1
  option_lower = 2
  option_higher = 3
  default = 1

@dataclass
class MMXCMOptions(OptionDict, PerGameCommonOptions):
  """
  MMXCMOptions is our data class that will represent the user options for 
  the Mega Man X: Command Mission world in Archipelago!
  """
  
  rebellion_medal_count: rebellion_medal_count
  encounter_rate: encounter_rate
  
