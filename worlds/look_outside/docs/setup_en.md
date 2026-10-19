# Overview

See the latest release [here!](https://github.com/Turese/LOArchipelagoPlugins/releases) 

This guide is compatible with version 1.2.3 Alpha

Make sure you have archipelago installed before you start playing.

This game uses archipelago version 0.6.7

# Setting up archipelago

As this game is not part of the core archipelago package, the apworld file will need to be installed in order to play.

Consult [the official archipelago setup guide](https://archipelago.gg/tutorial/Archipelago/setup_en) for information on downloading archipelago and [playing with custom worlds](https://archipelago.gg/tutorial/Archipelago/setup_en#playing-with-custom-worlds).

# Setting up Player options

These are the various player options you can select in the archipelago options creator:

## Ending Goal(s)

This YAML option allows the player to select their goal for the run. The player can mix and match as many goals as they desire.

The game has been modified to encourage the player to do everything they need to get access locations in one save file. If the player selected the yaml option to set the goal to multiple endings, then all of those endings must be achieved on the same save file. The player can check their progress towards their goal with an event in the third floor stairwell.

The different goal options are as follows:


### Failed Ritual

Go to the roof without giving the astronomers any correct offerings

### Flawed Ritual

Give the astronomers at least one correct offering and defeat them on the roof

### Perfect Ritual

Give the astronomers all four correct offerings and defeat them on the roof

### Screaming Sky Ending

Give the astronomers all four correct offerings and flee from their final form on the roof

### Promise Ending 

Give the astronomers all four correct offerings and defeat them on the roof after making a promise to Sybil

### Mask Ending 

Give the astronomers all four weird offerings and face the Masked Shadow on the roof

### XIN-AMON Ending

Give three correct offerings and a Guinea Pig to Beryl, and then defeat XIN-AMON on the roof

### Eternal Fate Ending

Give the Guinea Pig as any offering and face it on the roof

### Unity Ending

Kill Sybil and enter the red door in the observatory to learn the truth

### Final True Ending

Give the astronomers all four correct offerings, defeat them on the roof, then unleash the true power of your Meteor Strike!

### Words of Power Ending

Complete all crosswords for the secret key, then accept Wilhelmina’s offer in the Tomb of Crosswords

### Smooch the Sultan

Power up by kissing 49 or more enemies and then give the Sultan of Kissing a kiss (selecting this goal activates Casanova Mode + locations)

### Smooch The Visitor

Give the astronomers all four correct offerings, defeat them on the roof, then give the Visitor a kiss. (selecting this goal activates Casanova Mode + locations)

## Other Game Options

### Death Link

Enables death link. If the player gets a game over, then it will trigger a game over for any other player who is currently online that also has death link enabled, and vice versa.

## Progression Locations

### Include Friendly Fire Locations

If disabled, locations will not be rewarded for killing characters that are not hostile to the player. If enabled, then a location will be granted for defeating every single character with a selectable "attack" option on their encounter screen.

(Note: there are currently bugs in the vanilla game can crash the game when the player attacks the non-hostile cursed people in the boiler room, so locations for killing them are removed from the randomizer as of the current patch 1.2.3)

### Include Rat Friendly Fire Locations

Friendly fire for rats. If disabled, locations will not be rewarded for killing hostile rats that become friendly when the player or any of their party members wears the rusty crown.

### Include Rusty Crown Locations

If enabled, locations will be rewarded for the two gifts it is possible to get from rats when the rusty crown is worn.

### Include Nestor and Rafta's Quest

If enabled, locations for helping Rafta write a letter, as well as killing all of Nestor's body parts and the worms that spawn from them will be enabled. Note: the game has been modified so worm enemies will still spawn even if their corresponding body part has been killed. If this option is disabled, the Love Letter, Stationery, and Pen items will be removed from the item pool, making this quest impossible to complete.

### Include The Spider's Recruitment Quest

Activates locations related to recruiting the Spider

#### Exclude All Locations

If this option is selected, then locations will not be rewarded for defeating the five boss shades on each floor that spawn on high danger levels, nor for any enemies past the secret door under the stairwell.

#### Include Large Shades

If this option is selected, then locations will be rewarded for defeating the five boss shades on each floor that spawn on high danger levels. Interacting with the secret door under the stairwell will tell the player which shades they have not yet defeated.

#### Include Large Shades and Spider

If this option is selected, then locations will be rewarded for defeating the five boss shades on each floor that spawn on high danger levels, as well as venturing into the secret room under the stairs and defeating the Spider. 

#### Include Large Shades, Spider, and Crawling Shade

If this option is selected, then locations will be rewarded for defeating the five boss shades on each floor that spawn on high danger levels, as well as venturing into the secret room under the stairs and defeating the Spider, and defeating the Crawling Shade enemy that chases the player in the corridor before they meet the Spider.

### Include Mask Offering Locations

This controls whether locations in areas specific to the Mask ending are randomized: Glitch world, the entirety of floor 4, the basement pit, and the landlord's hidden room.

### Include Long Roommate Sidequests

This controls whether locations in areas specific to the roommate's apartment visit sidequests are randomized. This includes: Hellen's plant watering quest, Leigh's cell phone quest, and Dan's NeoDuo quest.

### Include Video Game Skill Locations

If enabled, the skills rewarded for completing video games will be randomized, and a location will be granted after playing each video game at least once. If disabled, each game skill will be rewarded after only one play of its respective video game.

### Allow Killing Mutt and Eugene

If this is enabled, then the player will be able to kill Mutt and Eugene whenever they want to steal their stock. If this is disabled, the option to attack them will disabled in-game. Nestor is still attackable when posessing Eugene, but Eugene will survive the encounter.

### Include Door Encounter Locations

If this is enabled, locations will be rewarded for gifts and combat rewards granted from killing shopkeepers. If disabled, item rewards from door encounters will still be disabled.

Note: door shopkeepers are unaffected by this option. They still have their regular stock, though the Gamer will never sell video games and the Mystery Trader will never sell the key to the boss rush arena or any special currencies besides black ooze.

### Include Superbosses

If this is enabled, locations will be granted for defeating superbosses, as well as for gifts and overworld items that cannot be acquired without defeating superbosses.

The locations affected by this option are as follows:

- Glitch World - Slay Honko
  - Glitch World - Kiss Honko
- Teeth Hell - Slay Baby Teeth (Day 9+)
  - Teeth Hell - Baby Teeth Tunnel Item 1
  - Teeth Hell - Baby Teeth Tunnel Item 2
- Fungus Maze Depths - Defeat Swordmaster Comatus
  - Fungus Maze Depths - Kiss Swordmaster Comatus
  - Boiler Room - Learn Yoga From Comatus
- GF Break Room - Slay KOTD Characters
- Glitch World - Slay Slime Hydra
- Apt. 28 - Slay Drowning
- Sewer Center - Slay the Furnace
  - Sewer Center - Item Dropped by Furnace
- Sewer - Slay the Boiler Beast
- Mutt's Shop - Slay Mutt
- Meat World - Slay Sybil Core

Note that some of these locations may also be independently disabled by other game options.

### Casanova Mode

If this is enabled, casanova mode will be activated in-game, giving the player the option to kiss various enemy characters. Locations will be rewarded for each successful kiss.

## Item Randomization Options

### Include Test Armor/Test Swords

If enabled, the testsword and testarmor, both original and mkII, will be added to the item pool. Note: these items give massive attack and defense buffs to the point it makes most fights trivial.

### Randomize Player Arms

Player can decide if the player character start with both arms, left arm, right arm, or with no arms at all. The arms they didn't start with will be available as item drops in the multiworld.

### Starting Games

Which video games the player starts with.

#### Random 3

The player starts with 3 random video games

#### Vanilla

The player starts with the same 3 video games they would start with in the main game: Madwheels 97, Super Jump Lad, and Myrmidon.

### Floor-by-Floor Elevator Access

If enabled, the option to use the elevator will be granted to players one floor at a time rather than all at once. The elevator will always have the option to return to floor 3.

### Include Traps

If enabled, includes traps in the item pool

### Include Final True Ending Equipment

If enabled, adds equipment from the Visitor battle from the Final True Ending to the item pool.

Items affected:

- Heirloom Greatsword
- Demon Knuckles
- World Tree's Bane
- Sky Piercer
- Wizards' Staff
- Rabu Hammer
- Sword of Regicide
- Rotten Fang
- Ring of Torment

## Other options

### Rat Child Name

Picks what name the Rat Baby party member will have. The player will not get the opportunity to change this in-game. The default name is "Rat."

### Hide Overworld Items

Hides the identity of overworld items until after player picks them up; removes confirmation dialogue when picking up items.

# Installing the game client

The randomizer makes use of rpgmaker's plugins systems to connect to archipelago and randomize items.

### RPGmodder install

`LOAPClient.zip` has been optimized to be installed by [Zorkats' RPGModder](https://github.com/Zorkats/RPGModder). 

Download the RPGModder and follow the linked instructions, to install the mod and patch it over your copy of Look Outside

If the patch worked, booting up the game should show a new `Archipelago` menu option on the title screen.

Note: if you're having trouble getting the game to patch, ensure that your clean install of look outside does **not** include a folder titled "Mods". Make sure you re-run the Safe State Initialization process of RPGmodder after you remove the folder.

### Manual install

** WARNING: SAVE FILES MADE WITH THIS MOD MAY BE INCOMPATIBLE WITH A NON-MODDED VERSION OF THE GAME, AND MAY CAUSE CRASHES AFTER THE MOD IS UNINSTALLED **

This mod can also be installed without RPGModder

1. Unzip `LOAPClient.zip`. You should have a folder titled `Look Outside` (if not, then you can rename this folder to `Look Outside`)
2. Drag this folder over your Look Outside installation. This can be found at `\SteamLibrary\steamapps\common\Look Outside`
3. Add this text to the second to last line on the bottom of `\SteamLibrary\steamapps\common\Look Outside\js\plugins.js:`
    - It should be placed after everything in that file except for the `];` denoting the end of the object.

```
    ,{
      "name": "archipelago",
      "status": true,
      "description": "Archipelago.js build for Look Outside client",
      "parameters": {}
    },
    {
      "name": "LocationIds",
      "status": true,
      "description": "global variable mapping of all location ids",
      "parameters": {}
    },
    {
      "name": "NormalizeDifficulty",
      "status": true,
      "description": "Make the same locations available in all difficulties",
      "parameters": {}
    },
    {
      "name": "BackInTime",
      "status": true,
      "description": "Back in time: speak to the calendar to get the option to travel through time!",
      "parameters": {}
    },
    {
      "name": "BlackoutLamp",
      "status": true,
      "description": "If player interacts with the lamp after unlocking elevator, they can toggle blackout",
      "parameters": {}
    },
    {
      "name": "GoalChecker",
      "status": true,
      "description": "event in stairwell allowing player to check goal",
      "parameters": {}
    },
    {
      "name": "ShopHelpers",
      "status": true,
      "description": "helper function for overriding merchants and vending machines",
      "parameters": {}
    },
    {
      "name": "DoorHelpers",
      "status": true,
      "description": "Helper functions for tracking door encounter locations",
      "parameters": {}
    },
    {
      "name": "ToothHelpers",
      "status": true,
      "description": "helper functions for overriding tooth family events",
      "parameters": {}
    },
    {
      "name": "ItemImages",
      "status": true,
      "description": "Manages overworld item image overrides",
      "parameters": {}
    },
    {
      "name": "EventLogicUpdates",
      "status": true,
      "description": "Updates unique event logic",
      "parameters": {}
    },
    {
      "name": "MassEventUpdates",
      "status": true,
      "description": "Bulk operations on game events",
      "parameters": {}
    },
    {
      "name": "GoHome",
      "status": true,
      "description": "Menu option that sends you back to Apartment 33",
      "parameters": {}
    },
    {
      "name": "InsertAPItems",
      "status": true,
      "description": "Insert AP Items: Insert any item to players inventory by AP ID",
      "parameters": {}
    },
    {
      "name": "LookOutsideAPClient",
      "status": true,
      "description": "Archipelago Client for Look Outside",
      "parameters": {}
    },
    {
      "name": "ConnectionStatus",
      "status": true,
      "description": "connection status display",
      "parameters": {}
    },
    {
      "name": "MainMenuAPOptions",
      "status": true,
      "description": "New option in main menu to input AP room, player, password",
      "parameters": {}
    },
    {
      "name": "MassEventUpdates",
      "status": true,
      "description": "Updates overworld generic drops to have archipelago-specific text and images",
      "parameters": {}
    },
    {
      "name": "NormalizeDifficulty",
      "status": true,
      "description": "Make the same locations available in all difficulties",
      "parameters": {}
    },
    {
      "name": "ShopHelpers",
      "status": true,
      "description": "Helpers for updating the vending machines",
      "parameters": {}
    },
    {
      "name": "ToothHelpers",
      "status": true,
      "description": "Helpers for updating the tooth family events",
      "parameters": {}
    },
    {
      "name": "Unarmed",
      "status": true,
      "description": "Unarmed and Dangerous: Play as Sam with no arms!",
      "parameters": {}
    }
  ```

## Connecting to archipelago

If the game client is installed properly the main menu will have a new option titled `Archipelago`

This option will also be available in-game.

In order to connect to archipelago and start getting items, you will need to enter some information in this menu.

### Slot name

This will be the name you specified when setting up your game options

### Server

The server your game is hosted on. If your game is being hosted locally, you can enter this string to connect

`localhost`

Otherwise, the information you enter will typically be in the format:

`archipelago.gg:ROOMID`

### Password

The password for your room. If one was not specified on creation, this field can be left blank.

### Connection status

If all goes well, your game should automatically connect on updating your information in the Archipelago menu. Connection status will display in the top left corner. If connection fails, or you are disconnected from a play session, you can make another connection attempt by clicking on the connection status message.
