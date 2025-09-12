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

  # The player can choose which locations to remove from their AP.
  excluded_locations: PerPlayerOption[OptionDict] = PerPlayerOption(OptionDict, "Exclude Locations",
    options={
      "Special Sealed Area 1st Room MD 1": Toggle,
      "Special Sealed Area 1st Room MD 2": Toggle,
      "Special Sealed Area 1st Room MD 3": Toggle,
      "Special Sealed Area 1st Room MD 4": Toggle,
      "Special Sealed Area 1st Room MD 5": Toggle,
      "Special Sealed Area 1st Room MD 6": Toggle,
      "Special Sealed Area 1st Room MD 7": Toggle,
      "Special Sealed Area 1st Room MD 8": Toggle,
      "Special Sealed Area 1st Room MD 9": Toggle,
      "Special Sealed Area 1st Room MD 10": Toggle,
      "Special Sealed Area 2nd Room MD 1": Toggle,
      "Special Sealed Area 2nd Room MD 2": Toggle,
      "Special Sealed Area 2nd Room MD 3": Toggle,
      "Special Sealed Area 2nd Room MD 4": Toggle,
      "Special Sealed Area 2nd Room MD 5": Toggle,
      "Special Sealed Area 2nd Room MD 6": Toggle,
      "Special Sealed Area 2nd Room MD 7": Toggle,
      "Special Sealed Area 2nd Room MD 8": Toggle,
      "Special Sealed Area 2nd Room MD 9": Toggle,
      "Special Sealed Area 2nd Room MD 10": Toggle,
      "Special Sealed Area 3rd Room MD 1": Toggle,
      "Special Sealed Area 3rd Room MD 2": Toggle,
      "Special Sealed Area 3rd Room MD 3": Toggle,
      "Special Sealed Area 3rd Room MD 4": Toggle,
      "Special Sealed Area 3rd Room MD 5": Toggle,
      "Special Sealed Area 3rd Room MD 6": Toggle,
      "Special Sealed Area 3rd Room MD 7": Toggle,
      "Special Sealed Area 3rd Room MD 8": Toggle,
      "Special Sealed Area By Ninetales MD 1": Toggle,
      "Special Sealed Area By Ninetales MD 2": Toggle,
      "Special Sealed Area By Ninetales MD 3": Toggle,
      "Special Sealed Area By Ninetales MD 4": Toggle,
      "Special Sealed Area By Ninetales MD 5": Toggle,
      "Special Sealed Area By Ninetales MD 6": Toggle,
      "Special Sealed Area By Ninetales MD 7": Toggle,
      "Maze Area 1 Rafflesian MD 1": Toggle,
      "Maze Area 1 Rafflesian MD 2": Toggle,
      "Maze Area 1 Rafflesian MD 3": Toggle,
      "Missile Maintenance Room MD 1": Toggle,
    },
    default={}
  )
  
