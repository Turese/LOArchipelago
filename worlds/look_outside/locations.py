from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location
from worlds.look_outside.locations_consts import APT_33_LOCATIONS, LocationData, location_table, location_to_region

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
    pass
