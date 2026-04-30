from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from worlds.look_outside.locations import get_location_name

from .options import PlayerGoal
from worlds.look_outside.regions_consts import all_regions_table,\
    can_nestor_rafta, can_open_any_simple_lock
from rule_builder.rules import Has, And

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
    # game rules
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

    #f3 rules
    world.set_rule(world.get_location(get_location_name("APT_33_RECRUIT_PHILLIPPE", world)), Has("Phillippe's Remains"))
    world.set_rule(world.get_location(get_location_name("APT_33_RECRUIT_RAT_BABY", world)), Has("Rat Baby Thing"))
    world.set_rule(world.get_location(get_location_name("APT_33_BATHROOM_RECRUIT_ROACHES", world)), Has("Roach (Inventory Item)"))
    world.set_rule(world.get_location(get_location_name("APT_33_ROACH_QUEST", world)), Has("Roaches"))

    world.set_rule(world.get_location(get_location_name("F3_PLANTER_KEY", world)), Has("Lyle"))
    world.set_rule(world.get_location(get_location_name("F3_PLAYING_CARD", world)), Has("Xaria and Montgomery"))

    world.set_rule(world.get_location(get_location_name("APT_31_TELESCOPE_DISC_EXPOSURE", world)), Has("Void Disc"))

    world.set_rule(world.get_location(get_location_name("APT_32_CHILD_BEDROOM_BEN_PLAY", world)), Has("Army Guy Figure"))

    world.set_rule(world.get_location(get_location_name("APT_37_PROJECTOR_ROOM_PHOTO", world)), And(Has("Negative Disc"), Has("Photo Paper")))

    #locked safes
    world.set_rule(world.get_location(get_location_name("APT_31_BEDROOM_SAFE_ITEM", world)), can_open_any_simple_lock)
    world.set_rule(world.get_location(get_location_name("APT_32_MASTER_BEDROOM_SAFE_ITEM", world)), can_open_any_simple_lock)
    world.set_rule(world.get_location(get_location_name("APT_36_BEDROOM_SAFE_ITEM", world)), can_open_any_simple_lock)

    #nestor quest rules
    world.set_rule(world.get_location(get_location_name("F3_HAND_WORMS_COMBAT_VICTORY", world)), can_nestor_rafta)





def set_completion_condition(world: LookOutsideWorld) -> None:
    world.set_completion_rule(Has("Roof Access Key"))
