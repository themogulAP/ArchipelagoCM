#This imports all classes we need for the Logic behind the rules. 
from typing import TYPE_CHECKING, Any
from BaseClasses import CollectionState

#Importing all of our location data from locations.py to be added here,
#Then uses AP architecture to import add_rule.
from .Locations import MMXCMLocationData
from worlds.generic.Rules import add_rule

#Prevents the rules py from importing the entire world!
if TYPE_CHECKING:
    from . import MMXCMWorld

#Defining our Set Rules for our MMXCMWorld to be created in init.py
#Set rules is what "orders" the games rules. 
def set_rules(world: "MMXCMWorld"):
    for location, rule in get_rules_dict(world).items():
        add_rule(location, rule)
        
#This is the logic behind the rules we will set for each location. 
def get_rules_dict(world: "MMXCMWorld") -> dict[str, Any]:
    return {
