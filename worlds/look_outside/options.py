from Options import Choice, Toggle, PerGameCommonOptions, OptionGroup, NamedRange, OptionSet
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
    display_name = "Randomize Arms"
    option_start_armed = 0
    option_start_unarmed = 1
    option_start_left = 2
    option_start_right = 3
    default = 0

class IncludeFriendlyFire(Toggle):
    """This controls whether locations specific to attacking non-hostile
    characters and potential recruits are randomized. This includes all merchants."""
    display_name = "Include Friendly Fire"
    default = 0

class IncludeRustyCrown(Toggle):
    """This controls whether locations specific to interacting with rats are randomized. If toggled, then
    locations for killing any of the rats that become friendly to a player wearing the crown are excluded."""
    default = 0

class IncludeTestGear(Toggle):
    """Adds Test Armor and Test Swords to the item pool."""
    display_name = "Include Test Armor/Test Swords"
    default = 0

class IncludeNestorQuest(Toggle):
    """This controls whether locations specific to the Nestor and Rafta quest are randomized."""
    display_name = "Include Nestor and Rafta's Quest"
    option_none = 0
    option_body_parts = 1
    option_all_worms = 2
    default = 0

class IncludeShades(Toggle):
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
    default = 0

class IncludeRoommateQuests(Toggle):
    """This controls whether locations specific to various roommate quests are
    randomized: Dan, Hellen, and Leigh's quests."""
    default = 0

class LockpicksInLogic(Toggle):
    """This controls whether the lockpick items or simple key items are placed into the item pool.
    If lockpicks_only is selected, then they can be used in place of keys at any locked location,
    and Kaeley will not become upset if they are used in her puzzle room.
    Default both lockpicks and simple keys are placed in the pool."""
    display_name = "Lockpicks and keys"
    lockpicks_and_keys = 0
    lockpicks_only = 1
    keys_only = 2
    default = 0

class StartingGames(Choice):
    """This controls which games are available at the start of the game.
    Vanilla gives the player Super Jumplad, Madwheels 97, and Myrmidon"""
    display_name = "Starting Games"
    option_random_3 = 0
    option_vanilla = 1
    option_none = 2
    default = 0

class DeathLink(Toggle):
    """This controls death link enablement"""
    display_name = "Death Link"
    default = 0

"""
class Merchantsanity(OptionSet):
    Whether merchants have randomized items
    
    Overworld: Merchants  the overworld; Eugene and Mutt, and the secret rat shot if crown logic is selected
    Vending machines: Items accessible from vending machines, Audrey included
    Special currency: Shops that take currency other than cash; Rat Hole, Emmanuel, etc
    Door encounters: Merchants that arrive at the front door
    
    valid_keys = frozenset({
        Merchantsanity.queen_of_sauce, Merchantsanity.purchases,
        Merchantsanity.skills, Merchantsanity.friendship,
    })
    display_name = "Randomize Merchants"
    option_none = 0
    option_overworld_only = 1
    option_special_currency = 2
    option_all_merchants = 2
    default = 0

class RandomizedMerchantItems(NamedRange):
    Picks how many randomized items each merchant carries.
    range_start = 1
    range_end = 4
    default = 1
"""



@dataclass
class LookOutsideOptions(PerGameCommonOptions):
    goal: PlayerGoal
    include_arms: IncludeArms
    friendly_fire: IncludeFriendlyFire
    rusty_crown: IncludeRustyCrown
    include_test_gear: IncludeTestGear
    include_nestor_quest: IncludeNestorQuest
    include_shades: IncludeShades
    include_mask: IncludeMaskLocations
    include_roommate_quests: IncludeRoommateQuests
    lockpicks_in_logic: LockpicksInLogic
    starting_games: StartingGames
    death_link: DeathLink

option_groups = [
    OptionGroup(
        "Location Options",
        [PlayerGoal, IncludeFriendlyFire, IncludeRustyCrown, IncludeNestorQuest, IncludeShades,
         IncludeMaskLocations, IncludeRoommateQuests],
    ),
    OptionGroup(
        "Item Options",
        [IncludeTestGear, IncludeArms, LockpicksInLogic, StartingGames],
    ),
    OptionGroup("Other Options", [DeathLink])
]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    "default": {
        "goal": 1,
        "include_arms": 0,
        "friendly_fire": 0,
        "rusty_crown": False,
        "include_test_gear": False,
        "include_nestor_quest": False,
        "include_shades": False,
        "include_mask": "True",
        "include_roommate_quests": True,
        "lockpicks_in_logic": True,
        "starting_games": 1,
        "death_link": False
    },
}


