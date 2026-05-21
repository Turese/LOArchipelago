from Options import Choice, Toggle, PerGameCommonOptions, OptionGroup, NamedRange, OptionSet,\
    FreeText
from dataclasses import dataclass

class PlayerGoal(Choice):
    """Ending of the game required to win."""
    display_name = "Ending Goal"
    option_any_partial_ritual_ending = 0
    option_any_perfect_ritual_ending = 1
    option_screaming_skies = 2
    option_promise = 3
    option_mask = 4
    option_xin_amon = 5
    option_unity = 6
    option_all_roof_endings = 7
    option_all_endings = 9
    default = 3

class IncludeArms(Choice):
    """Adds the player character's arms to the item pool."""
    display_name = "Randomize Player Arms"
    option_start_armed = 0
    option_start_unarmed = 1
    option_start_left = 2
    option_start_right = 3
    default = 0

class IncludeFriendlyFire(Toggle):
    """This controls whether locations specific to attacking non-hostile
    characters and potential recruits are included. This includes all merchants, Spine, and Marc-André."""
    display_name = "Include Friendly Fire"

class IncludeRatFriendlyFire(Toggle):
    """This controls whether locations specific to attacking rats that become non-hostile
    when wearing the rusty crown are included."""
    display_name = "Include Rat Friendly Fire"

class IncludeRustyCrown(Toggle):
    """This controls whether locations specific to interacting with non-hostile rats are randomized."""

class IncludeTestGear(Toggle):
    """Adds Test Armor and Test Swords to the item pool."""
    display_name = "Include Test Armor/Test Swords"

class IncludeNestorQuest(Toggle):
    """This controls whether locations specific to the Nestor and Rafta quest are randomized."""
    display_name = "Include Nestor and Rafta's Quest"

class IncludeShades(Choice):
    """This controls whether locations specific to the Spider recruitment quest are randomized."""
    display_name = "Include the Spider's Recruitment Quest"
    option_none = 0
    option_large = 1
    option_large_spider = 2
    option_large_spider_crawling = 3
    default = 0

class IncludeMaskLocations(Toggle):
    """This controls whether locations specific to the
    Mask ending are randomized: Glitch world, floor 4, the basement pit,
    and the landlord's hidden room."""
    display_name = "Include Mask Offering Locations"

class IncludeRoommateQuests(Toggle):
    """This controls whether roommate quests that involve escorting them to their apartments are
    randomized: Dan, Hellen, and Leigh's quests."""
    display_name = "Include Long Roommate Sidequests"
    

class IncludeGameSkills(Toggle):
    """This controls whether the skills given by completing each of the video games are randomized."""
    display_name = "Randomize Video Game Skill Rewards"

class StartingGames(Choice):
    """This controls which games are available at the start of the game.
    Vanilla gives the player Super Jumplad, Madwheels 97, and Myrmidon"""
    display_name = "Starting Games"
    option_random_3 = 0
    option_vanilla = 1
    option_none = 2
    default = 2

class DeathLink(Toggle):
    """This controls death link enablement"""
    display_name = "Enable Death Link"
    display_name = "Death Link"
    
class RatBabyName(FreeText):
    """This controls rat baby's name, default is 'Rat' """
    display_name = "Rat Child Name"

class AllowKillingShopkeepers(Toggle):
    """This controls whether players are allowed to kill Eugene or Mutt to get their stuff. Default false"""
    display_name = "Allow Killing Mutt and Eugene"
    display_name = "Allow Killing Mutt/Eugene"

class RandomizeDoorEncounters(Toggle):
    """Randomize items from door encounters, including merchants. Default true"""
    display_name = "Randomize Door Encounter Items"


@dataclass
class LookOutsideOptions(PerGameCommonOptions):
    goal: PlayerGoal
    include_arms: IncludeArms
    friendly_fire: IncludeFriendlyFire
    rat_friendly_fire: IncludeRatFriendlyFire
    rusty_crown: IncludeRustyCrown
    include_test_gear: IncludeTestGear
    include_nestor_quest: IncludeNestorQuest
    include_shades: IncludeShades
    include_mask: IncludeMaskLocations
    include_roommate_quests: IncludeRoommateQuests
    include_game_skills: IncludeGameSkills
    #lockpicks_in_logic: LockpicksInLogic
    starting_games: StartingGames
    death_link: DeathLink
    rat_baby_name: RatBabyName
    allow_killing_shopkeepers: AllowKillingShopkeepers
    randomize_door_encounters: RandomizeDoorEncounters

option_groups = [
    OptionGroup(
        "Location Options",
        [PlayerGoal, IncludeFriendlyFire, IncludeRustyCrown, IncludeNestorQuest, IncludeShades,
         IncludeMaskLocations, IncludeRoommateQuests, IncludeGameSkills, RandomizeDoorEncounters],
    ),
    OptionGroup(
        "Item Options",
        [IncludeTestGear, IncludeArms, StartingGames], # LockpicksInLogic
    ),
    OptionGroup("Other Options", [DeathLink, RatBabyName])
]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    "default": {
        "goal": 1,
        "include_arms": 0,
        "friendly_fire": False,
        "rat_friendly_fire": False,
        "rusty_crown": True,
        "include_test_gear": False,
        "include_nestor_quest": False,
        "include_shades": 0,
        "include_mask": True,
        "include_roommate_quests": True,
        #"lockpicks_in_logic": True,
        "starting_games": 2,
        "include_game_skills": 1,
        "randomize_door_encounters": True,
        "allow_killing_shopkeepers": False,
        "death_link": False
    },
}


