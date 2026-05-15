from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import  Region
from worlds.look_outside.regions_consts import all_regions_table, region_name_groups

if TYPE_CHECKING:
    from .__init__ import LookOutsideWorld

def create_and_connect_regions(world: LookOutsideWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: LookOutsideWorld) -> None:
    regions = []

    excluded_regions = exclude_regions(world)

    for region_name in all_regions_table.keys():
        if region_name in excluded_regions:
            continue
        regions.append(Region(region_name, world.player, world.multiworld))

    world.multiworld.regions += regions
    print(all_regions_table["STAIRWELL"])


def connect_regions(world: LookOutsideWorld) -> None:
    excluded_regions = exclude_regions(world)
    excluded_exits = exclude_exits(world)


    for region_name, region_info in all_regions_table.items():
        if region_name in excluded_regions:
            continue
        region = world.get_region(region_name)
        for exit_name, exit_info in region_info.exits.items():
            if exit_info.target_region in excluded_regions:
                continue
            if exit_name in excluded_exits:
                continue
            target_region = world.get_region(exit_info.target_region)
            region.connect(target_region, exit_name, rule=exit_info.rule)


def exclude_regions(world: LookOutsideWorld) -> set[str]:
    exclude_set = set()
    if world.options.include_roommate_quests == 0:
        exclude_set.update(region_name_groups["ROOMMATE_QUEST"])
    if world.options.include_mask == 0:
        exclude_set.update(region_name_groups["MASK"])
    return exclude_set

def exclude_exits(world: LookOutsideWorld) -> set[str]:
    exclude_set = set()
    if world.options.allow_killing_shopkeepers == 1:
        exclude_set.update({ "MUTTS_COUNTER" })
        # if player is killing shopkeepers, we're going to assume theyre killing mutt to get his stuff
    return exclude_set