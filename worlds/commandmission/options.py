# This file is where every setting is defined that the player can choose, thus defining logic.
from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions

@dataclass
class MMXCMOptions(PerGameCommonOptions):
    """
    MMXCMOptions is our data class that will represent the user options for
    the Mega Man X: Command Mission world in Archipelago!
    """

    rebellion_medal_count: Range = Range(
        display_name="Rebellion Medal Count",
        internal_name="rebellion_medal_count",
        default=9,
        range_start=0,
        range_end=9
    )

    encounter_rate: Choice = Choice(
        display_name="Encounter Rate",
        internal_name="encounter_rate",
        options={"off": 0, "vanilla": 1, "lower": 2, "higher": 3},
        default=1
    )
