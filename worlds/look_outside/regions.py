from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import  Region
from worlds.look_outside.regions_consts import all_regions_table

if TYPE_CHECKING:
    from .__init__ import LookOutsideWorld

def create_and_connect_regions(world: LookOutsideWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: LookOutsideWorld) -> None:
    regions = []

    for region_name in all_regions_table.keys():
        regions.append(Region(region_name, world.player, world.multiworld))

    world.multiworld.regions += regions


def connect_regions(world: LookOutsideWorld) -> None:
    for region_name, region_info in all_regions_table.items():
        region = world.get_region(region_name)
        for exit_name, exit_info in region_info.exits.items():
            target_region = world.get_region(exit_info.target_region)
            region.connect(target_region, exit_name, rule=exit_info.rule)


