from Options import Choice, Toggle, PerGameCommonOptions, OptionGroup, NamedRange, OptionSet,\
    FreeText
from dataclasses import dataclass

"""
class PlayerGoal(Choice):
    ""Ending of the game required to win.""
    display_name = "Ending Goal"
    option_any_partial_ritual_ending = 0
    option_any_perfect_ritual_ending = 1
    option_screaming_sky = 2
    option_promise = 3
    option_mask = 4
    option_xin_amon = 5
    option_unity = 6
    option_true_final = 7
    option_all_roof_endings = 8
    option_all_endings = 9
    default = 3
"""

class PlayerGoal(OptionSet):
    """Goal(s) required in order to finish."""

    FAILED_RITUAL = "Failed Ritual"
    ANY_RITUAL = "Flawed Ritual"
    PERFECT_RITUAL = "Perfect Ritual"
    SCREAMING_SKY_ENDING = "Screaming Sky Ending"
    PROMISE_ENDING = "Promise Ending"
    MASK_ENDING = "Mask Ending"
    XIN_AMON_ENDING = "XIN-AMON Ending"
    ETERNAL_FATE_ENDING = "Eternal Fate Ending"
    UNITY_ENDING = "Unity Ending"
    TRUE_FINAL_ENDING = "True Final Ending"
    WORDS_OF_POWER_ENDING = "Words of Power Ending"
    #DEFEAT_DISASTER = "Boss Gauntlet: Defeat Disaster"
    #SMOOCH_THE_SULTAN = "Smooch the Sultan"

    display_name = "Ending Goal(s)"
    valid_keys = {
        FAILED_RITUAL,
        ANY_RITUAL,
        PERFECT_RITUAL,
        SCREAMING_SKY_ENDING,
        PROMISE_ENDING,
        MASK_ENDING,
        XIN_AMON_ENDING,
        ETERNAL_FATE_ENDING,
        UNITY_ENDING,
        TRUE_FINAL_ENDING,
        WORDS_OF_POWER_ENDING,
    }
    default=set([PROMISE_ENDING])
    def verify(self, world, player_name, plando_options):
        super().verify(world, player_name, plando_options)

        if not self.value:
            raise ValueError("At least one Ending Goal must be selected.")

class IncludeArms(Choice):
    """Adds the player character's arms to the item pool."""
    display_name = "Randomize Player Arms"
    option_start_with_both_arms = 0
    option_start_unarmed = 1
    option_start_with_left_arm = 2
    option_start_with_right_arm = 3
    default = 1

class IncludeFriendlyFire(Toggle):
    """This controls whether locations specific to attacking non-hostile
    characters and potential recruits are included. This includes all merchants, Spine, and Marc-André."""
    display_name = "Include Friendly Fire Locations"
    default = False

class IncludeRatFriendlyFire(Toggle):
    """This controls whether locations specific to attacking rats that become non-hostile
    when wearing the rusty crown are included."""
    display_name = "Include Rat Friendly Fire Locations"
    default = True

class IncludeRustyCrown(Toggle):
    """This controls whether locations specific to interacting with non-hostile rats are randomized."""
    display_name = "Include Rusty Crown Locations"
    default = True

class IncludeTestGear(Toggle):
    """Adds Test Armor and Test Swords to the item pool. These items are incredibly busted; they make most fights trivial."""
    display_name = "Include Test Armor/Test Swords"
    default = False

class IncludeNestorQuest(Toggle):
    """This controls whether locations specific to the Nestor and Rafta romance quest are randomized."""
    display_name = "Include Nestor and Rafta's Quest"
    default = True

class IncludeShades(Choice):
    """This controls whether locations specific to the Spider recruitment quest are randomized."""
    display_name = "Include the Spider's Recruitment Quest"
    option_exclude_all_locations = 0
    option_include_large_shades = 1
    option_include_large_shades_and_spider = 2
    option_include_large_shades_and_spider_and_crawling_shade = 3
    default = 0

class IncludeMaskLocations(Toggle):
    """When checked, areas specific to the
    Mask ending will be randomized: Glitch world, floor 4, the basement pit,
    and the landlord's hidden room."""
    display_name = "Include Mask Offering Locations"
    default = True

class IncludeRoommateQuests(Toggle):
    """When checked, items from roommate quests that involve escorting companions to their own apartments are
    randomized: Dan, Hellen, and Leigh's quests."""
    display_name = "Include Long Roommate Sidequests"
    default = True
    

class IncludeGameSkills(Toggle):
    """This controls whether the skills given by completing each of the video games are randomized."""
    display_name = "Include Video Game Skill Locations"
    default = True

class StartingGames(Choice):
    """This controls which games are available at the start of the game.
    Vanilla gives the player Super Jumplad, Madwheels 97, and Myrmidon"""
    display_name = "Starting Games"
    option_random_3 = 0
    option_vanilla = 1
    option_none = 2
    default = 2

class DeathLink(Toggle):
    """This controls death link enablement.
    If you game over, other players with death link enabled will also game over, and vice versa."""
    display_name = "Death Link"
    default = False
    
class RatBabyName(FreeText):
    """This controls the rat child's name, default is 'Rat'."""
    display_name = "Rat Child Name"
    default = "Rat"

class AllowKillingShopkeepers(Toggle):
    """This controls whether players are allowed to kill Eugene or Mutt to get their stuff. Default false"""
    display_name = "Allow Killing Mutt and Eugene"
    default = False

class IncludeDoorEncounters(Toggle):
    """Randomize items from door encounters, including merchants. Default true."""
    display_name = "Include Door Encounter Locations"
    default = True

class IncludeTraps(Toggle):
    """Adds traps to the item pool."""
    default = True
    display_name = "Include Traps"

class HideOverworldItems(Toggle):
    """Hides the identity of overworld items until they have been picked up."""
    default = False
    display_name = "Hide Overworld Items"

class IncludeSuperBosses(Toggle):
    """Includes locations for defeating superbosses 
    (Honko, Baby Teeth Day 9, Swordmaster Comatus, KOTD, Slime Hydra, Drowning, Godmutt, Boiler Beast, and Furnace)."""
    default = False
    display_name = "Include Superbosses"

class ElevatorByFloor(Toggle):
    """Elevator access is unlocked floor-by-floor rather than all at once."""
    default = True
    display_name = "Floor-by-Floor Elevator Access"

class StartingRoommates(NamedRange):
    """This controls how many roommates the player starts with. Default 0, maximum of 16 (all recruits)."""
    display_name = "Starting Roommates"
    range_start = 0
    range_end = 16
    default = 0


@dataclass
class LookOutsideOptions(PerGameCommonOptions):
    goal: PlayerGoal
    include_arms: IncludeArms
    include_friendly_fire: IncludeFriendlyFire
    include_rat_friendly_fire: IncludeRatFriendlyFire
    include_rusty_crown: IncludeRustyCrown
    include_test_gear: IncludeTestGear
    include_nestor_quest: IncludeNestorQuest
    include_shades: IncludeShades
    include_mask: IncludeMaskLocations
    include_roommate_quests: IncludeRoommateQuests
    include_game_skills: IncludeGameSkills
    starting_games: StartingGames
    starting_roommates: StartingRoommates
    elevator_by_floor: ElevatorByFloor
    death_link: DeathLink
    rat_baby_name: RatBabyName
    allow_killing_shopkeepers: AllowKillingShopkeepers
    include_door_encounters: IncludeDoorEncounters
    include_traps: IncludeTraps
    hide_overworld_items: HideOverworldItems
    include_superbosses: IncludeSuperBosses

option_groups = [
    OptionGroup(
        "Progression Locations",
        [IncludeFriendlyFire, IncludeSuperBosses, IncludeRustyCrown, IncludeRatFriendlyFire, IncludeNestorQuest, IncludeShades,
        IncludeMaskLocations, IncludeRoommateQuests, IncludeGameSkills, IncludeDoorEncounters, AllowKillingShopkeepers],
    ),
    OptionGroup(
        "Item Randomization Options",
        [IncludeTestGear, IncludeArms, IncludeTraps, ElevatorByFloor, StartingGames, StartingRoommates],
    ),
    OptionGroup("Other Options", [HideOverworldItems, RatBabyName])
]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    "default": {
        "goal": set([PlayerGoal.PROMISE_ENDING]),
        "include_arms": IncludeArms.option_start_unarmed,
        "include_friendly_fire": False,
        "include_rat_friendly_fire": False,
        "include_rusty_crown": True,
        "include_test_gear": False,
        "include_nestor_quest": False,
        "include_shades": IncludeShades.option_exclude_all_locations,
        "include_mask": True,
        "include_roommate_quests": True,
        "starting_games": StartingGames.option_none,
        "starting_roommates": 0,
        "elevator_by_floor": True,
        "include_game_skills": True,
        "include_door_encounters": True,
        "allow_killing_shopkeepers": False,
        "death_link": False,
        "include_superbosses": False
    },
}
