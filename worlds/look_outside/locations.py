from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location, LocationProgressType
from worlds.look_outside.locations_consts import location_name_groups, LocationData, location_table, location_to_region,\
    UNDER_THE_STAIRS_LOCATIONS
from worlds.look_outside.items_consts import LOItem
from worlds.look_outside.regions_consts import stairwell_planet_lock
from worlds.look_outside.rules_consts import can_perform_flawed_ritual,\
    can_perform_perfect_ritual, can_perform_mask_ritual, can_perform_eternal_fate_ritual,\
    can_perform_xin_amon_ritual, can_true_final_skill, can_true_final_game
from rule_builder.rules import Has
from worlds.look_outside.rules_consts import can_keep_promise
from worlds.look_outside.options import IncludeShades


if TYPE_CHECKING:
    from .__init__ import LookOutsideWorld


class LOLocation(Location): 
    game = "Look Outside" 

def get_location_id(location_data: LocationData) -> int:
    return location_data.id

def get_location_name(location_name: str, world: LookOutsideWorld) -> str:
    location_data = location_table[location_name]
    return location_data.str_name

def create_all_locations(world: LookOutsideWorld) -> None:
    create_regular_locations(world)
    create_events(world)
    exclude_locations(world)

def create_regular_locations(world: LookOutsideWorld) -> None:
    excluded_locations = exclude_locations(world)
    for location_id, location_info in location_table.items():
        if location_id in excluded_locations:
            continue
        parent_region_name = location_to_region[location_info.str_name]
        parent_region = world.get_region(parent_region_name)
        location = LOLocation(world.player, location_info.str_name, location_info.id, parent_region)
        parent_region.locations.append(location)

def create_events(world: LookOutsideWorld) -> None:
    world.get_region("STAIRWELL").add_event(
        "GROUND_FLOOR_STAIRWELL_DOOR", "OPENED_GROUND_FLOOR_FROM_STAIRWELL", rule=stairwell_planet_lock, location_type=LOLocation, item_type=LOItem
    )

    world.get_region("FLOOR_2_EAST").add_event("F2_ASTER", "MET_ASTER", location_type=LOLocation, item_type=LOItem)

    world.get_region("AURELIUS_CLOSET").add_event("F1_AURELIUS", "MET_AURELIUS", location_type=LOLocation, item_type=LOItem)

    world.get_region("GROUND_FLOOR_HALL_EAST").add_event("GF_JASPER", "MET_JASPER", location_type=LOLocation, item_type=LOItem)

    world.get_region("BASEMENT_WEST_PARKING_GARAGE").add_event(
        "B_BERYL", "MET_BERYL", location_type=LOLocation, item_type=LOItem
    )

    world.get_region("GROUND_FLOOR_HALL_EAST").add_event(
        "GF_MENS_BATHROOM_NESTOR", "MET_NESTOR", location_type=LOLocation, item_type=LOItem
    )
    world.get_region("GROUND_FLOOR_HALL_EAST").add_event(
        "GROUND_FLOOR_LOBBY", "BUS_CRASH", location_type=LOLocation, item_type=LOItem
    )
    world.get_region("FLOOR_1_MAZE").add_event(
        "F1_HALL", "MET_AUDREY", rule=Has("Advice Can Funds"), location_type=LOLocation, item_type=LOItem
    )

    world.get_region("F1_RUINED_APARTMENT").add_event(
        "RUINED_APT_PIPE", "MET_RAFTA", location_type=LOLocation, item_type=LOItem
    )

    world.get_region("APT_28_FLOODED_TWILIGHT").add_event(
        "TWILIGHT_CLOSET", "ACTIVATED_PIRANHAS", location_type=LOLocation, item_type=LOItem
    )

    world.get_region("APT_12_MAIN").add_event(
        "APT_12_BATHROOM", "MET_SPIDER_HUSK", location_type=LOLocation, item_type=LOItem
    )

    # todo: mutt is only killable when allowing fire on shopkeepers
    world.get_region("MUTTS_BACK_ROOM").add_event(
        "MUTT_BACK_DOOR", "KILLED_MUTT", location_type=LOLocation, item_type=LOItem
    )

    # ENDINGS

    world.get_region("APT_35_SIBYL").add_event(
        "SIBYL", "AWAKENED_SIBYL", rule=Has("Telescope"), location_type=LOLocation, item_type=LOItem
    )

    world.get_region("APT_12_UNITY_ROOM").add_event(
        "UNITY_ENDING_NOTE", "UNITY_ENDING", location_type=LOLocation, item_type=LOItem
    )

    world.get_region("CROSSWORD_DUNGEON").add_event("FREE_WILHELMINA", "WORDS_OF_POWER_ENDING")

    roof = world.get_region("ROOF")

    roof.add_event(
        "RITUAL_CIRCLE_NO_ASTRONOMERS", "FAILED_RITUAL_ENDING", location_type=LOLocation, item_type=LOItem
    )
    roof.add_event(
        "RITUAL_CIRCLE_SOME_OFFERINGS", "FLAWED_RITUAL_ENDING", rule=can_perform_flawed_ritual, location_type=LOLocation, item_type=LOItem
    )

    roof.add_event(
        "RITUAL_CIRCLE_PERFECT", "PERFECT_RITUAL_ENDING", rule=can_perform_perfect_ritual, location_type=LOLocation, item_type=LOItem
    ) # no distinction between truth and denial here. this should fire off upon killing the E4

    roof.add_event(
        "RITUAL_CIRCLE_PERFECT_PROMISE", "PROMISE_ENDING", rule=can_keep_promise, location_type=LOLocation, item_type=LOItem
    )

    roof.add_event(
        "RITUAL_CIRCLE_WEIRD_OFFERINGS", "MASK_ENDING", rule=can_perform_mask_ritual, location_type=LOLocation, item_type=LOItem
    )

    roof.add_event(
        "RITUAL_CIRCLE_GUINEA_PIG", "ETERNAL_FATE_ENDING", rule=can_perform_eternal_fate_ritual, location_type=LOLocation, item_type=LOItem
    )

    roof.add_event(
        "RITUAL_CIRCLE_GUINEA_PIG_PERFECT", "XIN_AMON_ENDING", rule=can_perform_xin_amon_ritual, location_type=LOLocation, item_type=LOItem
    )

    if world.options.include_game_skills == 1:
        roof.add_event(
            "RITUAL_CIRCLE_METEOR_STRIKE", "TRUE_FINAL_ENDING", rule=can_true_final_skill, location_type=LOLocation, item_type=LOItem
        )
    else:
        roof.add_event(
            "RITUAL_CIRCLE_METEOR_STRIKE", "TRUE_FINAL_ENDING", rule=can_true_final_game, location_type=LOLocation, item_type=LOItem
        )

    roof.add_event(
        "RITUAL_CIRCLE_PERFECT_FLEE", "SCREAMING_SKIES_ENDING", rule=can_perform_perfect_ritual, location_type=LOLocation, item_type=LOItem
    )

    # large shades

    world.get_region("FLOOR_3_HALL").add_event(
        "FLOOR_3_SHADE", "DEFEATED_FLOOR_3_SHADE", location_type=LOLocation, item_type=LOItem)

    # F2 east and west arent connected so they get separate shade entries
    world.get_region("FLOOR_2_EAST").add_event(
        "FLOOR_2_SHADE_EASTSIDE", "DEFEATED_FLOOR_2_SHADE_ON_EAST_SIDE", location_type=LOLocation, item_type=LOItem)
    
    world.get_region("FLOOR_2_WEST").add_event(
        "FLOOR_2_SHADE_WESTSIDE", "DEFEATED_FLOOR_2_SHADE_ON_WEST_SIDE", location_type=LOLocation, item_type=LOItem)
    
    world.get_region("FLOOR_1_MAZE").add_event(
        "FLOOR_1_SHADE", "DEFEATED_FLOOR_1_SHADE", location_type=LOLocation, item_type=LOItem)
    
    world.get_region("GROUND_FLOOR_HALL_EAST").add_event(
        "GF_SHADE", "DEFEATED_GF_SHADE", location_type=LOLocation, item_type=LOItem)

    world.get_region("BASEMENT_EAST").add_event(
        "BASEMENT_EAST_SHADE", "DEFEATED_BASEMENT_SHADE", location_type=LOLocation, item_type=LOItem)
    
def exclude_locations(world: LookOutsideWorld) -> None:
    exclude_set = set()
    if world.options.include_mask == 0:
        exclude_set.update(location_name_groups["MASK"])
    if world.options.include_roommate_quests == 0:
        exclude_set.update(location_name_groups["ROOMMATE_QUEST"])
    if world.options.friendly_fire == 0:
        exclude_set.update(location_name_groups["FRIENDLY_FIRE"])
    if world.options.rat_friendly_fire == 0:
        exclude_set.update(location_name_groups["RAT_FRIENDLY_FIRE"])
    if world.options.rusty_crown == 0:
        exclude_set.update(location_name_groups["RUSTY_CROWN"])
    if world.options.include_nestor_quest == 0:
        exclude_set.update(location_name_groups["NESTOR_QUEST"])
    if world.options.include_shades == IncludeShades.option_none:
        exclude_set.update(location_name_groups["LARGE_SHADE"])
        exclude_set.update(UNDER_THE_STAIRS_LOCATIONS.keys())
    elif world.options.include_shades == IncludeShades.option_large:
        exclude_set.update(UNDER_THE_STAIRS_LOCATIONS.keys())
    elif world.options.include_shades == IncludeShades.option_large_spider:
        exclude_set.add("STAIRS_CRAWLING_SHADE_COMBAT_VICTORY")
    if world.options.include_game_skills == 0:
        exclude_set.update(location_name_groups["GAME_SKILLS"])

    return exclude_set
