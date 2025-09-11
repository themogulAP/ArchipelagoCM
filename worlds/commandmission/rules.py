#This imports all classes we need for the Logic behind the rules. 
from typing import TYPE_CHECKING, Any
from BaseClasses import CollectionState

#Importing all of our location data from locations.py to be added here,
#Then uses AP architecture to import add_rule.
from .Locations import LOCATION_TABLE, MMXCMLocationData
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
    player = world.player
    rules = {}
   
   
    for location_name, location_data in LOCATION_TABLE.items():
        #Rule: For All locations in Lagrano Ruins to require the Lagrano Ruins Access Code. 
         if location_data["parent_region"] == "Lagrano Ruins":
             rules[location_name] = lambda state: state.has("Lagrano Ruins Access Code", player)

         elif location_data["parent_region"] == "Central Tower":
               rules[location_name] = lambda state: state.has("Central Tower Access Code", player)
             
         elif location_data["parent_region"] == "Tianna Camp":
               rules[location_name] = lambda state: state.has("Tianna Camp Access Code", player)

         elif location_data["parent_region"] == "Gaudile Laboratory":
               rules[location_name] = lambda state: state.has("Gaudile Laboratory Access Code", player)

         elif location_data["parent_region"] == "Ulfat Factory":
               rules[location_name] = lambda state: state.has("Ulfat Factory Access Code", player)

         elif location_data["parent_region"] == "Gimialla Mine":
               rules[location_name] = lambda state: state.has("Gimialla Mine Access Code", player)

         elif location_data["parent_region"] == "Vanallia Desert":
               rules[location_name] = lambda state: state.has("Vanallia Desert Access Code", player)
             
         elif location_data["parent_region"] == "Melda Ore Plant":
               rules[location_name] = lambda state: state.has("Melda Ore Plant Access Code", player)

         elif location_data["parent_region"] == "Grave Ruins Base":
               rules[location_name] = lambda state: state.has("Grave Ruins Base Access Code", player)
       
         elif location_data["parent_region"] == "Far East HQ":
               rules[location_name] = lambda state: state.has("Far East HQ Access Code", player)

    return rules
