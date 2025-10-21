
# Mega Man X Command Mission

## Where is the settings page?

The [player settings page for this game](../player-settings) contains all the options you need to configure and export a
config file.

## What does randomization do to this game?

When it comes to Mega Man X Command Mission, randomization changes the locations of:
~Currently implemented~
All Mystery Data (ground pickups via dashing through them)
Mechaniloids (Ex: Deerball, Wolfoid, etc.) 

~For Future Release~
- All Characters and parameters.
- All Sky Room Cosmetics (over 1000 more checks!)
- Traps
- and more!

## What items and locations get shuffled?

- All consumable items: Build Powers, Vaccine Program, etc.
- All Weapons: X Buster, Joker, Z Saber, etc.
- All Sub-Weapons: Stamina Missile, Vitality Missile, etc.
- All Force Metal: LE+1000, Decoy, X Heart, etc.
Way more to be introduced in future patches!

-------NEW ITEMS: Access Codes and Rebellion Medals-----
Access Codes allow the Central Tower Arcade room teleporter to be used! 
Once you receive these Access Codes, you will gain access to the representative stages! 

Here is a list:
Lagrano Ruins, Tianna Camp, Gaudile Laboratory, Ulfat Factory, Gimialla Mine, Vanallia Desert, Melda Ore Plant, Grave Ruins Base, Far East HQ
Note: The Central Tower access code will work slightly differently: it will patch out the WALL blocking from the rest of the chapter. 
- This is located in Air City gate... where the Green NPC And tape are located. (You can dash right through it when the access code is received!)

## Which items can be in another player's world?
- Consumables
- Weapons
- Sub Weapons
- Access Codes
- Force Metal

## What does another world's item look like in MMX Command Mission?

This will be implemented later! 

## When the player receives an item, what happens?

Items received in Luigi's Mansion will display a text overlay that does not interrupt gameplay.. 

## Changes from the vanilla game

###### Customization options:

- Add Plants into the pool as locations
- Add Portrait Ghosts into the pool as locations
- Add Speedy Spirits and Gold Mice into the pool as locations. These logically require the Blackout to be active to reach. The gold mice can be acquired out of logic before the blackout is available.
- Add Boos into the pool as locations and items
- Add Toads into the pool as locations
- Add almost every interactable object within the game into the pool as locations
- Require the player to have obtained enough money to get a specific rank upon completion.
- Customize the Boo count requirement for the Balcony and Secret Altar
- Customize the number of Mario's items needed to trigger the Fortune-teller
- Start with the stronger Poltergust or include it in the item pool
- Start with the Boo Radar or include it in the pool
- Start in the Hidden Mansion
- Randomize the ghost types in certain rooms of the mansion
- Randomize the type of enemies to be shuffled around
- Randomize your starting location so you don't always start in the Foyer
- Randomize which doors are open or closed by default
- Randomize the models the door use (in other words change the look for the doors themselves).
- Randomize how chests look when they contain items.
- Enable hints to various locations including Madame Clarivoya, Toads, and the telelphones
- Enable scanning Portrait ghost's hearts to get additional hints
- Randomize Boo health, Boo Speed (how fast they move around), Boo Escape time (how long before they leave the current room),
Boo Anger (if you want boos to stay passive or get aggressive and attack Luigi), and Extra Boo Spots 
(add more spots for Boos to hide in furniture).


###### Quality of life:

- Save anywhere by pressing Down on the Dpad + B (as long as blackout is not on and if you are NOT in a boss fight)
- Various streamlining tweaks (removed cutscenes, dialogue, transitions, and animations)
- The 1F Washroom boo gate has been removed in favor of simply locking the door.
- Many events have had text changed to better represent the state or events of the randomizer
- Breaker Room starts locked unless Door Rando is on
- In-game hints for the locations of items appear on Toads, Telephones and Madame Clairvoya
- Boolossus will not spawn if you do not have Ice Element Medal
- The Blackout can be toggled from the breaker in the breaker room, to access certain locations of the game.
- (Optional) Turn off Fear and Pickup animations for Luigi
- (Optional) Increase Luigi's innate movement speed.
- (Optional) Randomize music
- (Optional) Change Luigi's Max Health
- (Optional) Change King Boo's health (final boss)
- (Optional) Energy Link support (I.e., Allows money to be sent to the Archipelago Server as energy)
- Credit to discord user rishingfod for out Luigi's Mansion client icon

###### Quality of death:

- (optional) Death Link support. (I.e., if Luigi is defeated, everyone else participating in death link also dies)
- (optional) Trap Link support (I.e., If Luigi finds a trap, everyone else participating in trap link also gets a trap)

###### Energy Link:

Energy link allows players to send and receive money as energy to other energy-linked team members through commands sent through the LMClient.
The energy link conversion rate is 5e3:1 (energy:currency) of Luigi's worth. (worth is used when determining the rank requirement)

For example, requesting 50000 energy will send Luigi two Bills (20,000 each) and two Coins (5000 each), for a total worth of 50,000.

Commands are:
- `/send_energy <amount>` - Sends energy to the Archipelago server to be consumed by any player on the team.
- `/request_energy <amount>` - Requests energy from the Archipelago server, reducing the available amount up to the requested value.
- `/display_energy` - Displays the current energy available to your team
- `/energy_link` - Toggles Energy Link settings for the player's existing session.
