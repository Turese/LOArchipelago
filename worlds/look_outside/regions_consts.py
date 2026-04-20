
from rule_builder.rules import Has, HasAll, Rule, Or, And

from worlds.look_outside.items import item_name_groups

from .options import PlayerGoal
from typing_extensions import NamedTuple
from worlds.celeste_open_world.data.CelesteLevelData import all_regions

can_access_roof = Has("Roof Access Key")

stairwell_planet_lock = Or(HasAll("Mars Disc", "Earth Disc"), HasAll("Sun Disc", "Negative Disc"))

# Perfect offering requirements
has_complete_manuscript = Has("Progressive Loose Manuscript", count=2)
has_painting = Has("Correct Painting")
has_photo = Has("Correct Photograph")
has_cctv = Has("Correct CCTV Recording")

# Any perfect offering (at least one of the four, with correct counts)
has_any_perfect_offering = Or(has_complete_manuscript, has_painting, has_photo, has_cctv) 
# All perfect offerings (all four, with correct counts)
has_all_perfect_offerings = And(has_complete_manuscript, has_painting, has_photo, has_cctv)

can_open_any_simple_lock = Or(Has("Lockpicks"), Has("Simple Key", count=20))  # todo: count keys
can_access_stairwell = Has("Padlock Key")
can_access_elevator = Has("Elevator Activation")
can_access_floor_2_east = can_access_stairwell
can_access_floor_2_west = can_access_elevator
can_awaken_sibyl = HasAll("Telescope", "Apt. 35 Key")
can_access_floor_1 = Or(And(can_access_floor_2_east, Has("Apt. 21 Key")), can_awaken_sibyl)
can_access_ground_floor = Or(can_access_elevator, And(can_access_stairwell, stairwell_planet_lock))
can_access_apt_21_depths = Or(And(can_access_floor_1, Has("Herbicide"), Has("Jasper's Key")), can_awaken_sibyl)
can_access_basement = Or(can_access_elevator, And(can_access_stairwell, Has("Basement Key")))
can_access_floor_4 = can_access_elevator
can_access_metro = And(can_access_floor_4, Has("Metro Ticket"))
can_access_glitch_world = Has("Unlabeled Cartridge")

can_perform_flawed_ritual = And(can_access_roof, has_any_perfect_offering)
can_perform_perfect_ritual = And(can_access_roof, has_all_perfect_offerings)
can_true_final = And(can_perform_perfect_ritual, Has("Meteor Strike"))
can_keep_promise = And(can_perform_perfect_ritual, can_awaken_sibyl)
can_reach_unity = And(can_access_apt_21_depths, Has("Small Red Key"))
can_perform_mask_ritual = And(can_access_roof, HasAll(*item_name_groups["MASK_OFFERING"]))

# Eternal fate = all guinea pig rituals shy of xin-amon
can_perform_eternal_fate_ritual = And(Has("Guinea Pig"), can_perform_flawed_ritual)
# Xin Amon ritual: all perfect offerings except CCTV, and Guinea Pig
can_perform_xin_amon_ritual = And(can_perform_eternal_fate_ritual, has_complete_manuscript, has_painting, has_photo)

can_words_of_power = And(HasAll("Book of Crossword Puzzles", "Pluto Disc"), can_access_basement)


class ExitData(NamedTuple):
    target_region: str
    rule: Rule | None = None

    
class RegionData(NamedTuple):
    exits: dict[str, ExitData]
    locations: set[str] = set()


f3_regions_table: dict[str, RegionData] = {
    "APT_33": RegionData(
        exits={
            "APT_33_FRONT_DOOR": ExitData("FLOOR_3_HALL"),
        },
    ),
    "FLOOR_3_HALL": RegionData(
        exits={
            "F3_STAIRWELL_DOOR": ExitData("STAIRWELL", rule=can_access_stairwell),
        },
    ),
}

stairwell_regions_table: dict[str, RegionData] = {
    "STAIRWELL": RegionData(
        exits={
            "ROOF_DOOR": ExitData("ROOF", rule=can_access_roof),
        }
    ),
    "ROOF": RegionData(
        exits={}
    ),
}

all_regions_table = {**f3_regions_table, **stairwell_regions_table}