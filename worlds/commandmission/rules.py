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

    
    world.multi_world.item_rules["Far East HQ Access Code"] = lambda state: state.has_group("Rebellion Medals", player, world.options.rebellion_medal_count.value)

    rules.update({
        # Extra rules for Lagrano Ruins ------------
        "East Area Stairs 4F to 5F MD 1": lambda state: state.has("Lagrano Key", player),
        "East Area Stairs 4F to 5F MD 2": lambda state: state.has("Lagrano Key", player),
        "East Area Stairs 4F to 5F MD 3": lambda state: state.has("Lagrano Key", player),
        
         # Continue adding Central Tower here-------
        "Special Sealed Area 1st Room MD 1": lambda state: state.has("Central Key", player),
        "Special Sealed Area 1st Room MD 2": lambda state: state.has("Central Key", player),
        "Special Sealed Area 1st Room MD 3": lambda state: state.has("Central Key", player),
        "Special Sealed Area 1st Room MD 4": lambda state: state.has("Central Key", player),
        "Special Sealed Area 1st Room MD 5": lambda state: state.has("Central Key", player),
        "Special Sealed Area 1st Room MD 6": lambda state: state.has("Central Key", player),
        "Special Sealed Area 1st Room MD 7": lambda state: state.has("Central Key", player),
        "Special Sealed Area 1st Room MD 8": lambda state: state.has("Central Key", player),
        "Special Sealed Area 1st Room MD 9": lambda state: state.has("Central Key", player),
        "Special Sealed Area 1st Room MD 10": lambda state: state.has("Central Key", player),
        
        "Special Sealed Area 2nd Room MD 1": lambda state: state.has("Central Key", player),
        "Special Sealed Area 2nd Room MD 2": lambda state: state.has("Central Key", player),
        "Special Sealed Area 2nd Room MD 3": lambda state: state.has("Central Key", player),
        "Special Sealed Area 2nd Room MD 4": lambda state: state.has("Central Key", player),
        "Special Sealed Area 2nd Room MD 5": lambda state: state.has("Central Key", player),
        "Special Sealed Area 2nd Room MD 6": lambda state: state.has("Central Key", player),
        "Special Sealed Area 2nd Room MD 7": lambda state: state.has("Central Key", player),
        "Special Sealed Area 2nd Room MD 8": lambda state: state.has("Central Key", player),
        "Special Sealed Area 2nd Room MD 9": lambda state: state.has("Central Key", player),
        "Special Sealed Area 2nd Room MD 10": lambda state: state.has("Central Key", player),
        
        "Special Sealed Area 3rd Room MD 1": lambda state: state.has("Central Key", player),
        "Special Sealed Area 3rd Room MD 2": lambda state: state.has("Central Key", player),
        "Special Sealed Area 3rd Room MD 3": lambda state: state.has("Central Key", player),
        "Special Sealed Area 3rd Room MD 4": lambda state: state.has("Central Key", player),
        "Special Sealed Area 3rd Room MD 5": lambda state: state.has("Central Key", player),
        "Special Sealed Area 3rd Room MD 6": lambda state: state.has("Central Key", player),
        "Special Sealed Area 3rd Room MD 7": lambda state: state.has("Central Key", player),
        "Special Sealed Area 3rd Room MD 8": lambda state: state.has("Central Key", player),
        
        "Special Sealed Area By Ninetales MD 1": lambda state: state.has("Central Key", player),
        "Special Sealed Area By Ninetales MD 2": lambda state: state.has("Central Key", player),
        "Special Sealed Area By Ninetales MD 3": lambda state: state.has("Central Key", player),
        "Special Sealed Area By Ninetales MD 4": lambda state: state.has("Central Key", player),
        "Special Sealed Area By Ninetales MD 5": lambda state: state.has("Central Key", player),
        "Special Sealed Area By Ninetales MD 6": lambda state: state.has("Central Key", player),
        "Special Sealed Area By Ninetales MD 7": lambda state: state.has("Central Key", player),
        
        # Continue adding Tianna here-------
        "Maze Area 1 Behind Key MD 1": lambda state: state.has("Tianna Key", player),
        "Maze Area 1 Rafflesian MD 1": lambda state: state.has("Tianna Key", player),
        "Maze Area 1 Rafflesian MD 2": lambda state: state.has("Tianna Key", player),
        "Maze Area 1 Rafflesian MD 3": lambda state: state.has("Tianna Key", player),

        # Continue adding Gimialla Mine here------
        "L2 Southwest Division MD 1": lambda state: state.has("Booster Parts", player),
        "L2 Southeast Division MD 2": lambda state: state.has("Booster Parts", player),
        "L2 Northeast Division MD 1": lambda state: state.has("Booster Parts", player),
        "L2 Northeast Division MD 3": lambda state: state.has("Mega Mantor", player),
        "L3 Main Tunnel Blue Miner Trade Complete": lambda state: state.has("Blue Pickaxe", player),
        "L3 Northwest Division Red Miner Trade Complete": lambda state: state.has("Red Pickaxe", player),
        "L3 Northwest Division Yellow Miner Trade Complete": lambda state: state.has("Yellow Pickaxe", player), 
        "L3 Northeast Division Green Miner Trade Complete": lambda state: state.has("Green Pickaxe", player),
        "L3 Southwest Division MD 1": lambda state: state.has("Gimialla Key", player) and state.has("Heavy Motor", player) or state.has("Gold Blader", player),
        "L3 Southwest Division MD 2": lambda state: state.has("Gimialla Key", player),
        "L3 Southwest Division MD 3": lambda state: state.has("Gimialla Key", player),
        "Level 4 Main Tunnel MD 1": lambda state: state.has("Electric Components", player),
        "Level 4 Main Tunnel MD 2": lambda state: state.has("Electric Components", player),
        "Level 4 Main Tunnel MD 3": lambda state: state.has("Electric Components", player),
        "Level 4 Main Tunnel MD 4": lambda state: state.has("Electric Components", player),
        "Level 4 Main Tunnel MD 5": lambda state: state.has("Electric Components", player),
        "Level 4 Main Tunnel MD 6": lambda state: state.has("Electric Components", player),
        "Level 4 Main Tunnel MD 7": lambda state: state.has("Electric Components", player),
        "Level 4 Durability Lab MD 1": lambda state: state.has("Electric Components", player),
        "Level 4 Durability Lab MD 2": lambda state: state.has("Electric Components", player),
        "Level 4 Durability Lab MD 3": lambda state: state.has("Electric Components", player),

          # Continue adding Melda Ore Planet Here---------
        "B1 Entrance Hall MD 2": lambda state: state.has("Melda Key", player),
        "B1 Entrance Hall MD 3": lambda state: state.has("Melda Key", player),
        "B1 Entrance Hall MD 4": lambda state: state.has("Melda Key", player),
        "Missile Maintenance Room MD 1": lambda state: state.has("Melda Key", player),

        # Mehaniloid Locations---------
        "Deerball": lambda state: state.has("Lagrano Key", player) and state.has("Lagrano Ruins Access Code", player),
        "Radar Killer": lambda state: state.has("Tianna Key", player) and state.has("Tianna Camp Access Code", player),
        "Blowfish": lambda state: state.has("Mini Battery", player, 3) and state.has("Tianna Camp Access Code", player),
        "Big Monkey": lambda state: state.has("Gaudile Laboratory Access Code", player),
        "Preon": lambda state: state.has("Gaudile Laboratory Access Code", player),
        "Dober Man": lambda state: state.has("Gaudile Laboratory Access Code", player) and state.has("Bone Key", player),
        "Mettaur": lambda state: state.has("Gaudile Laboratory Access Code", player),
        "Einhammer": lambda state: state.has("Ulfat Factory Access Code", player) and state.has("Ball & Chain Hammer", player),
        "Killer Mantis": lambda state: state.has("Ulfat Factory Access Code", player),
        "Rush Loader": lambda state: state.has("Ulfat Factory Access Code", player),
        "Mega Mantor": lambda state: state.has("Gimialla Mine Access Code", player) and state.has("Mini Battery", player, 3),
        "Degraver": lambda state: state.has("Gimialla Mine Access Code", player),
        "Bat Bone": lambda state: state.has("Gimialla Mine Access Code", player),
        "Gold Blader": lambda state: state.has("Gimialla Mine Access Code", player) and state.has("Heavy Motor", player) and state.has("Gimialla Key", player),
        "Liquid Glob": lambda state: state.has("Vanallia Desert Access Code", player) and state.has("Cyber Liquid", player),
        "Mega Tortoise": lambda state: state.has("Vanallia Desert Access Code", player) and state.has("Mini Battery", player, 3),
        "Pararoid": lambda state: state.has("Vanallia Desert Access Code", player) and state.has("Mini Motor", player),
        "Meltdown": lambda state: state.has("Melda Ore Plant Access Code", player) and state.has("Melda Key", player),
        "Rabbid": lambda state: state.has("Melda Ore Plant Access Code", player),
        "Bladey": lambda state: state.has("Grave Ruins Base Access Code", player),

    })
        
    return rules
