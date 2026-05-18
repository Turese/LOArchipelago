from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from worlds.look_outside.locations import get_location_name
from worlds.look_outside.regions import exclude_regions

from .options import PlayerGoal

from worlds.look_outside.items_consts import item_name_groups, \
    num_multiple_items

from worlds.look_outside.regions_consts import all_regions_table
from worlds.look_outside.rules_consts import can_nestor_rafta, can_open_any_simple_lock, can_access_basement, can_leigh_quest
from rule_builder.rules import Has, And, HasAll, HasAny, Or
from worlds.look_outside.locations_consts import location_name_groups

if TYPE_CHECKING:
    from .__init__ import LookOutsideWorld


def set_all_rules(world: LookOutsideWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: LookOutsideWorld) -> None:
    excluded_regions = exclude_regions(world)
 
    for region_info in all_regions_table.values():
        for exit_name, exit_info in region_info.exits.items():
            if exit_info.target_region not in excluded_regions and exit_info.rule is not None:
                world.set_rule(world.get_entrance(exit_name), exit_info.rule)


def set_all_location_rules(world: LookOutsideWorld) -> None:
    # game rules
    if world.options.include_game_skills != 0:
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_WAKE_THE_BLOOD_KNIGHT", world)), Has("Wake the Blood Knight"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_WIZARDS_HELL", world)), Has("Wizards Hell: Arcane Tears"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_SUPER_JUMPLAD", world)), Has("Super Jumplad"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_SUPER_JUMPLAD_3", world)), Has("Super Jumplad 3"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_CATAFALQUE", world)), Has("Catafalque"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_HONKOS_GRAND_JOURNEY", world)), Has("Honko's Grand Journey"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_MADWHEELS_97", world)), Has("Madwheels 97"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_WRAITHSCOURGE", world)), Has("Wraithscourge"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_MASSACRE_PRINCESS", world)), Has("Massacre Princess"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_KILL_TO_SHOOT", world)), Has("Kill to Shoot"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_MYRMIDON", world)), Has("Myrmidon"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_SCREAMATORIUM", world)), Has("Screamatorium"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_FROGIT_ABOUT_IT", world)), Has("Frogit About It"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_BLOOD_GHOUL_ORGY_3", world)), Has("Blood Ghoul Orgy 3"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_OCTOCOOK", world)), Has("Octocook"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_SPACE_TRUCKERZ", world)), Has("Space Truckerz"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_REPTILE_FOOTBALL", world)), Has("Reptile Football"))
        world.set_rule(world.get_location(get_location_name("GAME_SKILL_CROSSWORD_CHALLENGE", world)), Has("Auntie Wilma's Crossword Challenge"))

    # f3 rules
    world.set_rule(world.get_location(get_location_name("APT_33_RECRUIT_PHILLIPPE", world)), Has("Phillippe's Remains"))
    world.set_rule(world.get_location(get_location_name("APT_33_RECRUIT_RAT_BABY", world)), Has("Rat Baby Thing"))
    world.set_rule(world.get_location(get_location_name("APT_33_BATHROOM_RECRUIT_ROACHES", world)), Has("Roach (Inventory Item)"))
    world.set_rule(world.get_location(get_location_name("APT_33_ROACH_QUEST", world)), Has("Roaches"))

    world.set_rule(world.get_location(get_location_name("F3_PLANTER_KEY", world)), Has("Lyle"))
    world.set_rule(world.get_location(get_location_name("F3_PLAYING_CARD", world)), Has("Xaria and Montgomery"))

    world.set_rule(world.get_location(get_location_name("APT_31_TELESCOPE_DISC_EXPOSURE", world)), Has("Void Disc"))

    world.set_rule(world.get_location(get_location_name("APT_32_CHILD_BEDROOM_BEN_PLAY", world)), Has("Army Guy Figure"))

    world.set_rule(world.get_location(get_location_name("APT_32_BATHROOM_RECRUIT_JOEL", world)), HasAll("Teddy", "Door Knob"))

    world.set_rule(world.get_location(get_location_name("APT_37_PROJECTOR_ROOM_PHOTO", world)), And(Has("Negative Disc"), Has("Photo Paper")))

    # f2 rules
    world.set_rule(world.get_location(get_location_name("F2_RECRUIT_ASTER", world)), And(Has("MET_AURELIUS"), Has("MET_JASPER"), can_access_basement))  # todo: event for meeting astronomers instead?
    
    if world.options.include_roommate_quests != 0:
        world.set_rule(world.get_location(get_location_name("F2_GRASSHOPPER_COMBAT_VICTORY", world)), can_leigh_quest)

    world.set_rule(world.get_location(get_location_name("APT_20_HYDRA_LAUNDRY", world)), HasAll("Jeanne's Laundry", "OPENED_GROUND_FLOOR_FROM_STAIRWELL"))

    world.set_rule(world.get_location(get_location_name("APT_21_DARK_ROOM_PHOTO", world)), Has("Exposed Paper"))
    world.set_rule(world.get_location(get_location_name("APT_21_SECOND_KISS_GIFT", world)), Has("Exposed Paper"))

    world.set_rule(world.get_location(get_location_name("APT_27_COMPLETE_MANUSCRIPT", world)), Has("Progressive Loose Manuscript"))

    if (world.options.allow_killing_shopkeepers == 1):
        world.set_rule(world.get_location(get_location_name("APT_24_REPTILE_FOOTBALL", world)), Has("Two Hundred Dollars")) # 75c each

    # f1 rules

    world.set_rule(world.get_location(get_location_name("F1_AUDREY_RECRUIT", world)), And(Has("Vending Machine Key"), Has("Advice Can Funds", count=num_multiple_items["Advice Can Funds"])))

    # gf rules

    world.set_rule(world.get_location(get_location_name("MUTT_SPIDER_HUSK_HEART", world)), Has("MET_SPIDER_HUSK"))
    
    world.set_rule(world.get_location(get_location_name("GF_KOTD_COMBAT_VICTORY", world)), HasAll(*item_name_groups["KOTD_FIGURE"]))
    if world.options.include_mask != 0:
        world.set_rule(world.get_location(get_location_name("GLITCH_SLIME_HYDRA_COMBAT_VICTORY", world)), HasAll(*item_name_groups["KOTD_FIGURE"]))

    # one more piranhas fight, dragonfish + 2x piranhas, is defeatable before piranhas activated. 
    # player will fight only the dragonfish, but the victory will still count.
    world.set_rule(world.get_location(get_location_name("APT_28_PIRANHAS_COMBAT_VICTORY", world)), Has("ACTIVATED_PIRANHAS"))
    world.set_rule(world.get_location(get_location_name("APT_28_GARBAGE_PIRANHAS_COMBAT_VICTORY", world)), Has("ACTIVATED_PIRANHAS"))
    world.set_rule(world.get_location(get_location_name("APT_28_TWILIGHT_PIRANHAS_COMBAT_VICTORY", world)), Has("ACTIVATED_PIRANHAS"))

    # locked safes
    world.set_rule(world.get_location(get_location_name("APT_31_BEDROOM_SAFE_ITEM", world)), can_open_any_simple_lock)
    world.set_rule(world.get_location(get_location_name("APT_32_MASTER_BEDROOM_SAFE_ITEM", world)), can_open_any_simple_lock)
    world.set_rule(world.get_location(get_location_name("APT_36_BEDROOM_SAFE_ITEM", world)), can_open_any_simple_lock)
    world.set_rule(world.get_location(get_location_name("APT_21_CLOSET_SAFE", world)), can_open_any_simple_lock)
    world.set_rule(world.get_location(get_location_name("APT_24_SAFE_ITEM", world)), can_open_any_simple_lock)
    world.set_rule(world.get_location(get_location_name("FRED_TOXIC_ROOM_SAFE", world)), can_open_any_simple_lock)
    world.set_rule(world.get_location(get_location_name("APT_18_E_SAFE_ITEM", world)), can_open_any_simple_lock)
    world.set_rule(world.get_location(get_location_name("CORNER_STORE_STORAGE_SAFE", world)), can_open_any_simple_lock)
    world.set_rule(world.get_location(get_location_name("MAILROOM_N_SAFE", world)), can_open_any_simple_lock)
    world.set_rule(world.get_location(get_location_name("LL_BEDROOM_SAFE", world)), can_open_any_simple_lock)

    # nestor quest rules
    if world.options.include_nestor_quest != 0:
        for location_id in location_name_groups["NESTOR_QUEST"]:
            world.set_rule(world.get_location(get_location_name(location_id, world)), can_nestor_rafta)
    
    if world.options.rusty_crown != 0:
        for location_id in location_name_groups["RUSTY_CROWN"]:
            world.set_rule(world.get_location(get_location_name(location_id, world)), Has("Rusty Crown"))

    # bus rules? since stairwell and bus are different areas, need to make sure player has seen bus before they can fight crawCrawlDelayAndRequestRateCrawlDelayAndRequestRateTes
    world.set_rule(world.get_location(get_location_name("STAIRWELL_CRAWLER_COMBAT_VICTORY", world)), Has("BUS_CRASH"))
    
    # basement rules

    world.set_rule(world.get_location(get_location_name("SECURITY_CORRECT_RECORDING", world)), And(Has("Guinea Pig"), HasAny("Blank VHS tape", "Incorrect CCTV Recording", "Correct CCTV Recording")))

    # audrey rules

    # ive earmarked different coin drops for different audrey locations
    # dollar coins for audrey items
    # and special quarter packs for advice cans
    # player will likely have far more than needed when they get this point
    world.set_rule(world.get_location(get_location_name("MUTT_VENDING_MACHINE_KEY", world)), HasAll("MET_AUDREY", "Advice Can Funds"))

    for location_id in location_name_groups["AUDREY_PURCHASE"]:
        world.set_rule(world.get_location(get_location_name(location_id, world)), Or(Has("Dollar Coin", count=num_multiple_items["Dollar Coin"]), Has("Dollar Coin", count=num_multiple_items["Two-Dollar Coin"])))

    world.set_rule(world.get_location(get_location_name("APT_30_TAXIDERMY_AUDREY_LOOT", world)), Has("Audrey"))
    world.set_rule(world.get_location(get_location_name("APT_28_SHRIMP_KNIGHT_AUDREY_LOOT", world)), Has("Audrey"))
    world.set_rule(world.get_location(get_location_name("LL_MEMORIAL_TANK_AUDREY_LOOT", world)), Has("Audrey"))
    world.set_rule(world.get_location(get_location_name("LL_TRENCH_DIGGER_AUDREY_LOOT", world)), Has("Audrey"))
    world.set_rule(world.get_location(get_location_name("LL_BATTLEFIELD_APC_AUDREY_LOOT", world)), Has("Audrey"))
    world.set_rule(world.get_location(get_location_name("B_CAR_HELLRIDE_AUDREY_LOOT", world)), Has("Audrey"))

    # vending machine rules
    world.set_rule(world.get_location(get_location_name("F3_VENDING_MACHINE_CHIPS", world)), Has("Vending Machine Snack Money", count=num_multiple_items["Vending Machine Snack Money"])) # 75c each
    world.set_rule(world.get_location(get_location_name("F3_VENDING_MACHINE_SPICY", world)), Has("Vending Machine Snack Money", count=num_multiple_items["Vending Machine Snack Money"])) # 75c each
    world.set_rule(world.get_location(get_location_name("F3_VENDING_MACHINE_GUMMI_BEARS", world)), Has("Vending Machine Snack Money", count=num_multiple_items["Vending Machine Snack Money"])) # 75c each
    world.set_rule(world.get_location(get_location_name("F3_VENDING_MACHINE_CHEESE", world)), Has("Vending Machine Snack Money", count=num_multiple_items["Vending Machine Snack Money"])) # 75c each
    world.set_rule(world.get_location(get_location_name("F3_VENDING_MACHINE_ONIONOS", world)), Has("Vending Machine Snack Money", count=num_multiple_items["Vending Machine Snack Money"])) # 75c each
    world.set_rule(world.get_location(get_location_name("F3_VENDING_MACHINE_ONIONOS", world)), Has("Vending Machine Snack Money", count=num_multiple_items["Vending Machine Snack Money"])) # 75c each
    world.set_rule(world.get_location(get_location_name("GF_COFFEE_MACHINE_MERCHANT", world)), Has("Vending Machine Snack Money", count=num_multiple_items["Vending Machine Snack Money"])) # 1.50 each
    world.set_rule(world.get_location(get_location_name("GF_CANDY_MACHINE_MERCHANT", world)), Has("Vending Machine Snack Money", count=num_multiple_items["Vending Machine Snack Money"])) # 25c each; assuming player will have some money leftover

    # special merchant rules
    for location_id in location_name_groups["CASSETTE_TAPE"]:
        world.set_rule(world.get_location(get_location_name(location_id, world)), Has("Cassette Tape", count=num_multiple_items["Cassette Tape"]))
    for location_id in location_name_groups["WORM_EGG"]:
        world.set_rule(world.get_location(get_location_name(location_id, world)), Has("Worm Egg", count=num_multiple_items["Worm Egg"]))
    for location_id in location_name_groups["RAT_TAIL"]:
        world.set_rule(world.get_location(get_location_name(location_id, world)), Has("Rat Tail", count=num_multiple_items["Rat Tail"]))
    for location_id in location_name_groups["BLACK_OOZE"]:
        world.set_rule(world.get_location(get_location_name(location_id, world)), Has("Black Ooze", count=num_multiple_items["Black Ooze"]))


flawed_ritual_endings = {"FLAWED_RITUAL_ENDING", "SCREAMING_SKIES_ENDING", "ETERNAL_FATE_ENDING", "XIN_AMON_ENDING", "MASK_ENDING"}

perfect_rituals = {"PERFECT_RITUAL_ENDING", "PROMISE_ENDING", "TRUE_FINAL_ENDING"}

all_rituals = {*flawed_ritual_endings, *perfect_rituals}

all_roof_endings = {*all_rituals, "FAILED_RITUAL_ENDING"}

all_endings = {*all_roof_endings, "UNITY_ENDING", "WORDS_OF_POWER_ENDING"}

def set_completion_condition(world: LookOutsideWorld) -> None:
    player_goal = world.options.goal
    if player_goal == PlayerGoal.option_all_endings:
        world.set_completion_rule(HasAll(*all_endings))
    elif player_goal == PlayerGoal.option_all_roof_endings:
        world.set_completion_rule(HasAll(*all_roof_endings))
    elif player_goal == PlayerGoal.option_any_partial_ritual_ending:
        world.set_completion_rule(HasAny(*all_rituals))
    elif player_goal == PlayerGoal.option_any_perfect_ritual_ending:
        world.set_completion_rule(HasAny(*perfect_rituals))
    elif player_goal == PlayerGoal.option_screaming_skies:
        world.set_completion_rule(Has("SCREAMING_SKIES_ENDING"))
    elif player_goal == PlayerGoal.option_promise:
        world.set_completion_rule(Has("PROMISE_ENDING"))
    elif player_goal == PlayerGoal.option_mask:
        world.set_completion_rule(Has("MASK_ENDING"))
    elif player_goal == PlayerGoal.option_xin_amon:
        world.set_completion_rule(Has("XIN_AMON_ENDING"))
    elif player_goal == PlayerGoal.option_unity:
        world.set_completion_rule(Has("UNITY_ENDING"))
