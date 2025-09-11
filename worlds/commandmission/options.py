# This file is where every setting is defined that the player can choose, thus defining logic.
from dataclasses import dataclass
from Options import Toggle, PerPlayerOption, Range, Choice, DeathLink, OptionDict, NamedRange, DefaultOn 

@dataclass
class MMXCMOptions(OptionDict):
  """
  MMXCMOptions is our data class that will represent the user options for 
  the Mega Man X: Command Mission world in Archipelago!
  """

  # Setting the # of Rebellion Medals the player needs to access Chapter 10.
  rebellion_medal_count: PerPlayerOption[Range] = PerPlayerOption(Range, "Rebellion Medal Count",
    default=9,
    range_start=0,
    range_end=9,
  )

  #This is the Option choice for the player's desired encounter rate.
  encounter_rate: Choice = Choice("Encounter Rate",
    {
      "vanilla": 0,
      "lower": 1,
      "higher": 2,
    },
    default="vanilla"
  )
