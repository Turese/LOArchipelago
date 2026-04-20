from __future__ import annotations

from typing import TYPE_CHECKING

from typing import NamedTuple
from BaseClasses import Location

from enum import IntFlag, auto


if TYPE_CHECKING:
    from .__init__ import LookOutsideWorld


class LocationCat(IntFlag):
    OVERWORLD_ITEM = auto()
    SKILL_UNLOCK = auto()
    RECRUIT = auto()
    COMBAT_VICTORY = auto()  # combat victory for aggressive npcs
    FRIENDLY_FIRE = auto() # combat victory for nonaggressive npcs
    MERCHANT = auto()
    DOOR_MERCHANT = auto()  # merchants that appear at the door
    EVENT_ITEM = auto()
    LOOT = auto()

class DifficultyCat(IntFlag):
    EXPLORER = auto()
    SURVIVOR = auto()
    CURSED = auto()

class LocationData(NamedTuple):
    str_id: str
    category: LocationCat
    id: int
    difficulty_lock: set[str] = set()

APT_33_LOCATIONS: dict[str, LocationData] = {
    "Apt. 33 Living Room - Item on Coffee Table": LocationData("APT_33_LIVING_ROOM_CASH", LocationCat.OVERWORLD_ITEM, 1),
    "Apt. 33 Living Room - Item on Shelf": LocationData("APT_33_LIVING_ROOM_SCREAMATORIUM", LocationCat.EVENT_ITEM, 2),
    "Apt. 33 Bathroom - Item on Counter": LocationData("APT_33_BATHROOM_FIRST_AID_KIT", LocationCat.OVERWORLD_ITEM, 3),
}

def get_location_parent_region(location_name: str, world: LookOutsideWorld) -> str:
    if (APT_33_LOCATIONS.get(location_name)): 
        return world.get_region("APT_33")

location_table = APT_33_LOCATIONS

class LOLocation(Location): 
    game = "Look Outside" 

def get_location_id(location_data: LocationData) -> int:
    return location_data.id

def create_all_locations(world: LookOutsideWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: LookOutsideWorld) -> None:
    for location_name, location_info in location_table.items():
        parent_region = get_location_parent_region(location_name, world)
        location = LOLocation(world.player, location_name, location_info.id, parent_region)
        parent_region.locations.append(location)

def create_events(world: LookOutsideWorld) -> None:
    pass
