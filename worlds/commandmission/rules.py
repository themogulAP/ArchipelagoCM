#This imports all classes we need for the Logic behind the rules. 
from typing import TYPE_CHECKING, Any

#Importing all of our location data from locations.py to be added here,
#Then uses AP architecture to import add_rule.
from .locations import LOCATION_TABLE
from worlds.generic.Rules import add_rule, add_item_rule
from .helpers import ACCESS_CODES_DATA

# Creating a class to be called later called ItemGroup
class ItemGroup:
    def __init__(self, name: str, item_names: frozenset[str]):
        self.name = name
        self.item_names = item_names

#This defines our group from items and locations of medals so we can check if the player has enough. 
REBELLION_MEDALS_GROUP = ItemGroup("Rebellion Medals", frozenset({
    "Rebellion Medal 1",
    "Rebellion Medal 2",
    "Rebellion Medal 3",
    "Rebellion Medal 4",
    "Rebellion Medal 5",
    "Rebellion Medal 6",
    "Rebellion Medal 7",
    "Rebellion Medal 8",
    "Rebellion Medal 9"
}))

REQUIRED_ACCESS_CODES = ItemGroup("9 Access Codes", frozenset({
    "Lagrano Ruins Access Code",
    "Central Tower Access Code",
    "Tianna Camp Access Code",
    "Gaudile Laboratory Access Code",
    "Ulfat Factory Access Code",
    "Gimialla Mine Access Code",
    "Vanallia Desert Access Code",
    "Melda Ore Plant Access Code",
    "Grave Ruins Base Access Code"
}))

#Prevents the rules py from importing the entire world!
if TYPE_CHECKING:
    from . import MMXCMWorld

#Set rules is what "orders" the games rules. 
#This will also provide us the means to lock Chapter 10 behind rebellion medals. 
def set_rules(world: "MMXCMWorld"):
    # Iterate through all locations to find the one that contains the
    # "Far East HQ Access Code" item.
    for location in world.multiworld.get_locations(world.player):
        # Check if the location has our specific item.
        if location.item and location.item.name == "Far East HQ Access Code":
            # Now, apply the rule to the location itself.
            add_rule(location, lambda state:
            state.has_group("9 Access Codes", world.player) and
            state.has_group("Rebellion Medals", world.player, world.options.rebellion_medal_count.value))
            break  # We found the item's location, so we can stop searching.

    # This loop remains the same, applying rules to specific locations.
    for location_name, rule in get_rules_dict(world).items():
        add_rule(world.multiworld.get_location(location_name, world.player), rule)

    # Prevent other access codes and important key items from being placed in the Far East HQ region.
    far_east_hq_region = world.multiworld.get_region("Far East HQ", world.player)
    # Use the keys from the imported ACCESS_CODES_DATA dictionary.
    non_far_east_access_codes = {code for code in ACCESS_CODES_DATA.keys() if code != "Far East HQ Access Code"}
    for location in far_east_hq_region.locations:
        add_item_rule(location, lambda item: item.name not in non_far_east_access_codes)

    for location in far_east_hq_region.locations:
        add_item_rule(location, lambda item: item.name != "Electric Components")

#This is the logic behind the rules we will set for each location.
def get_rules_dict(world: "MMXCMWorld") -> dict[str, Any]:
    player = world.player
    rules = {}

    for location_name, location_data in LOCATION_TABLE.items():
         #Rule: For All locations in Lagrano Ruins to require the Lagrano Ruins Access Code. 
        if location_data.parent_region == "Lagrano Ruins":
             rules[location_name] = lambda state: state.has("Lagrano Ruins Access Code", player)

        elif location_data.parent_region == "Central Tower Full":
               rules[location_name] = lambda state: state.has("Central Tower Access Code", player)

        elif location_data.parent_region == "Tianna Camp":
               rules[location_name] = lambda state: state.has("Tianna Camp Access Code", player)

        elif location_data.parent_region == "Gaudile Laboratory":
               rules[location_name] = lambda state: state.has("Gaudile Laboratory Access Code", player)

        elif location_data.parent_region == "Ulfat Factory":
               rules[location_name] = lambda state: state.has("Ulfat Factory Access Code", player)

        elif location_data.parent_region == "Gimialla Mine":
               rules[location_name] = lambda state: state.has("Gimialla Mine Access Code", player)

        elif location_data.parent_region == "Vanallia Desert":
               rules[location_name] = lambda state: state.has("Vanallia Desert Access Code", player)

        elif location_data.parent_region == "Melda Ore Plant":
               rules[location_name] = lambda state: state.has("Melda Ore Plant Access Code", player)

        elif location_data.parent_region == "Grave Ruins Base":
               rules[location_name] = lambda state: state.has("Grave Ruins Base Access Code", player)

        elif location_data.parent_region == "Far East HQ":
               rules[location_name] = lambda state: state.has("Far East HQ Access Code", player)

        # Add the new rule for the end-game event
        elif location_name == "Defeated Great Redips":
                rules[location_name] = lambda state: state.has("Far East HQ Access Code", player)

        # This prevents the endless loop and tells the AP where Far East Access Code CAN BE!
    for location_name, location_data in LOCATION_TABLE.items():
        if location_data.parent_region != "Far East HQ":
            add_item_rule(world.multiworld.get_location(location_name, world.player),
                            lambda i: i.name == "Far East HQ Access Code",
                            combine="or")

        #--------------------------- --- Specific rules based on required keys/items -------------------------------------------------

        # Lagrano Key Locations
        elif location_name in ["East Area Stairs 4F to 5F Tank Parts", "East Area Stairs 4F to 5F Figure Token 1", "East Area Stairs 4F to 5F Figure Token 2"]:
            rules[location_name] = lambda state: state.has("Lagrano Key", player)

        # Central Key Locations
        elif location_name in [
            "Special Sealed Area 1st Room Enter The Intruder", "Special Sealed Area 1st Room The Throne", "Special Sealed Area 1st Room Capital",
            "Special Sealed Area 1st Room Battle Epsilon", "Special Sealed Area 1st Room Epsilon 1", "Special Sealed Area 1st Room Ruins Passageway",
            "Special Sealed Area 1st Room The End", "Special Sealed Area 1st Room Epsilon 2", "Special Sealed Area 1st Room Display Device",
            "Special Sealed Area 1st Room Grave Ruins", "Special Sealed Area 2nd Room Flying Mechs", "Special Sealed Area 2nd Room Redips Soldier",
            "Special Sealed Area 2nd Room Aerial Assault", "Special Sealed Area 2nd Room Dragoon", "Special Sealed Area 2nd Room The Chair",
            "Special Sealed Area 2nd Room Transform Ability", "Special Sealed Area 2nd Room Transforming Mech", "Special Sealed Area 2nd Room Coliseum",
            "Special Sealed Area 2nd Room Battle Redips", "Special Sealed Area 2nd Room Judgment", "Special Sealed Area 3rd Room Redips 1",
            "Special Sealed Area 3rd Room Space", "Special Sealed Area 3rd Room Epsilon", "Special Sealed Area 3rd Room Redips 2",
            "Special Sealed Area 3rd Room Redips 3", "Special Sealed Area 3rd Room Tails", "Special Sealed Area 3rd Room Parts",
            "Special Sealed Area 3rd Room Scores Settled", "Special Sealed Area By Ninetales Great Redips", "Special Sealed Area By Ninetales Tails Front",
            "Special Sealed Area By Ninetales Tails Back", "Special Sealed Area By Ninetales X's Weapons", "Special Sealed Area By Ninetales Zero's Weapons",
            "Special Sealed Area By Ninetales Cinnamon's Weapons", "Special Sealed Area By Ninetales Massimo's Weapons"
        ]:
            rules[location_name] = lambda state: state.has("Central Key", player)

        # Tianna Key Locations
        elif location_name in ["Maze Area 1 Behind Key Tank Parts", "Maze Area 1 Rafflesian Figure Token 1", "Maze Area 1 Rafflesian Figure Token 2", "Maze Area 1 Rafflesian Ultimate Armor"]:
            rules[location_name] = lambda state: state.has("Tianna Key", player)

        # Gimialla Mine Keys & Items
        elif location_name in ["L2 Southwest Division Mini Motor", "L2 Southeast Division Figure Token", "L2 Northeast Division Tank Parts"]:
            rules[location_name] = lambda state: state.has("Booster Parts", player)
        elif location_name == "L2 Northeast Division Build LE":
            rules[location_name] = lambda state: state.has("Mega Mantor", player)
        elif location_name == "L3 Main Tunnel Blue Miner Trade Complete":
            rules[location_name] = lambda state: state.has("Blue Pickaxe", player)
        elif location_name == "L3 Northwest Division Red Miner Trade Complete":
            rules[location_name] = lambda state: state.has("Red Pickaxe", player)
        elif location_name == "L3 Northwest Division Yellow Miner Trade Complete":
            rules[location_name] = lambda state: state.has("Yellow Pickaxe", player)
        elif location_name == "L3 Northeast Division Green Miner Trade Complete":
            rules[location_name] = lambda state: state.has("Green Pickaxe", player)
        elif location_name in ["L3 Southwest Division Figure Token 1", "L3 Southwest Division Figure Token 2"]:
            rules[location_name] = lambda state: state.has("Gimialla Key", player)
        elif location_name == "L3 Southwest Division Tank Parts":
            rules[location_name] = lambda state: state.has("Gimialla Key", player) and state.has("Heavy Motor", player) and state.has("Gold Blader", player)
        elif location_name in ["Level 4 Main Tunnel Tank Energy 100", "Level 4 Main Tunnel Gain Hyper", "Level 4 Main Tunnel Build Power", "Level 4 Main Tunnel Build Armor", "Level 4 Main Tunnel Build Shield", "Level 4 Main Tunnel Build Speed", "Level 4 Main Tunnel Build WE", "Level 4 Durability Lab Water Guard", "Level 4 Durability Lab Thunder Guard", "Level 4 Durability Lab Fire Guard"]:
            rules[location_name] = lambda state: state.has("Electric Components", player)

        # Melda Ore Plant Key
        elif location_name in ["B1 Entrance Hall Figure Token 1", "B1 Entrance Hall Figure Token 2", "B1 Entrance Hall Figure Token 3", "Missile Maintenance Room Absolute Zero"]:
            rules[location_name] = lambda state: state.has("Melda Key", player)

        # Mehaniloid Location Rules
        elif location_name == "Deerball":
            rules[location_name] = lambda state: state.has("Lagrano Key", player) and state.has("Lagrano Ruins Access Code", player)
        elif location_name == "Radar Killer":
            rules[location_name] = lambda state: state.has("Tianna Key", player) and state.has("Tianna Camp Access Code", player)
        elif location_name == "Blowfish":
            rules[location_name] = lambda state: state.has("Mini Battery", player, 3) and state.has("Tianna Camp Access Code", player)
        elif location_name == "Big Monkey":
            rules[location_name] = lambda state: state.has("Gaudile Laboratory Access Code", player)
        elif location_name == "Preon":
            rules[location_name] = lambda state: state.has("Gaudile Laboratory Access Code", player)
        elif location_name == "Dober Man":
            rules[location_name] = lambda state: state.has("Gaudile Laboratory Access Code", player) and state.has("Bone Key", player)
        elif location_name == "Mettaur":
            rules[location_name] = lambda state: state.has("Gaudile Laboratory Access Code", player)
        elif location_name == "Einhammer":
            rules[location_name] = lambda state: state.has("Ulfat Factory Access Code", player) and state.has("Ball & Chain Hammer", player)
        elif location_name == "Killer Mantis":
            rules[location_name] = lambda state: state.has("Ulfat Factory Access Code", player)
        elif location_name == "Rush Loader":
            rules[location_name] = lambda state: state.has("Ulfat Factory Access Code", player)
        elif location_name == "Mega Mantor":
            rules[location_name] = lambda state: state.has("Gimialla Mine Access Code", player) and state.has("Mini Battery", player, 3)
        elif location_name == "Degraver":
            rules[location_name] = lambda state: state.has("Gimialla Mine Access Code", player)
        elif location_name == "Bat Bone":
            rules[location_name] = lambda state: state.has("Gimialla Mine Access Code", player)
        elif location_name == "Gold Blader":
            rules[location_name] = lambda state: state.has("Gimialla Mine Access Code", player) and state.has("Heavy Motor", player) and state.has("Gimialla Key", player)
        elif location_name == "Liquid Glob":
            rules[location_name] = lambda state: state.has("Vanallia Desert Access Code", player) and state.has("Cyber Liquid", player)
        elif location_name == "Mega Tortoise":
            rules[location_name] = lambda state: state.has("Vanallia Desert Access Code", player) and state.has("Mini Battery", player, 3)
        elif location_name == "Pararoid":
            rules[location_name] = lambda state: state.has("Vanallia Desert Access Code", player) and state.has("Mini Motor", player)
        elif location_name == "Meltdown":
            rules[location_name] = lambda state: state.has("Melda Ore Plant Access Code", player) and state.has("Melda Key", player)
        elif location_name == "Rabbid":
            rules[location_name] = lambda state: state.has("Melda Ore Plant Access Code", player)
        elif location_name == "Bladey":
            rules[location_name] = lambda state: state.has("Grave Ruins Base Access Code", player)

    return rules
