from typing import TYPE_CHECKING
from BaseClasses import CollectionState

from .Locations import MMXCMLocationData
from worlds.generic.Rules import add_rule

if TYPE_CHECKING:
    from . import MMXCMWorld

def set_rules(world: "MMXCMWorld"):
    for location, rule in get_rules_dict(world).items():
        add_rule(location, rule)
        
def get_rules_dict(world: "MMXCMWorld") -> dict[str, Any]:
    return {
