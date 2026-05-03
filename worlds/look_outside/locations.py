from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location
from worlds.look_outside.locations_consts import APT_33_LOCATIONS, LocationData, location_table, location_to_region
from worlds.look_outside.items import LOItem
from worlds.look_outside.regions_consts import stairwell_planet_lock
from rule_builder.rules import Has


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
        "SIBYL", "AWAKEN_SIBYL", rule=Has("Telescope"), location_type=LOLocation, item_type=LOItem
    )

    world.get_region("APT_12_UNITY_ROOM").add_event(
        "UNITY_ENDING_NOTE", "UNITY_ENDING", location_type=LOLocation, item_type=LOItem
    )
