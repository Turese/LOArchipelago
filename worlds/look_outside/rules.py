from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter

from .options import PlayerGoal
from worlds.look_outside.regions_consts import all_regions_table
from rule_builder.rules import Has

if TYPE_CHECKING:
    from .__init__ import LookOutsideWorld

def set_all_rules(world: LookOutsideWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: LookOutsideWorld) -> None:
    for region_info in all_regions_table.values():
        for exit_name, exit_info in region_info.exits.items():
            if exit_info.rule is not None:
                world.set_rule(world.get_entrance(exit_name), exit_info.rule)

def set_all_location_rules(world: LookOutsideWorld) -> None:
    pass

def set_completion_condition(world: LookOutsideWorld) -> None:
    world.set_completion_rule(Has("Roof Access Key"))
