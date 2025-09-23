# This file is where every setting is defined that the player can choose, thus defining logic.
from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions

# Define each option as its own class first.
class RebellionMedalCount(Range):
    display_name = "Rebellion Medal Count"
    internal_name = "rebellion_medal_count"
    default=9
    range_start=0
    range_end=9

class EncounterRate(Choice):
    display_name = "Encounter Rate"
    internal_name = "encounter_rate"
    option_off = 0
    option_vanilla = 1
    option_lower = 2
    option_higher = 3
    default = 1

# The dataclass then uses these classes directly as a container.
@dataclass
class MMXCMOptions(PerGameCommonOptions):
    """
    MMXCMOptions is our data class that will represent the user options for
    the Mega Man X: Command Mission world in Archipelago!
    """
    rebellion_medal_count: RebellionMedalCount
    encounter_rate: EncounterRate

# This is the dictionary that __init__.py will import.
options = {
    "rebellion_medal_count": RebellionMedalCount,
    "encounter_rate": EncounterRate
}
