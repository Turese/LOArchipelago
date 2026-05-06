from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location
from worlds.look_outside.locations_consts import LocationData, location_table, location_to_region
from worlds.look_outside.items import LOItem
from worlds.look_outside.regions_consts import stairwell_planet_lock
from worlds.look_outside.rules_consts import can_perform_flawed_ritual,\
    can_perform_perfect_ritual, can_perform_mask_ritual, can_perform_eternal_fate_ritual,\
    can_perform_xin_amon_ritual, can_true_final
from rule_builder.rules import Has
from worlds.look_outside.rules_consts import can_keep_promise


if TYPE_CHECKING:
    from .__init__ import LookOutsideWorld


class LOLocation(Location): 
    game = "Look Outside" 

def get_location_id(location_data: LocationData) -> int:
    return location_data.id

def get_location_name(location_name: str, world: LookOutsideWorld) -> str:
    location_data = location_table[location_name]
    if False: # todo: check cursed mode version modifier
        return location_data.cursed_name
    return location_data.str_name

def create_all_locations(world: LookOutsideWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: LookOutsideWorld) -> None:
    for location_id, location_info in location_table.items():
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

    roof.add_event(
        "RITUAL_CIRCLE_METEOR_STRIKE", "TRUE_FINAL_ENDING", rule=can_true_final, location_type=LOLocation, item_type=LOItem
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
    