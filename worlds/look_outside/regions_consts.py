from rule_builder.rules import Has, HasAll, Rule, Or, And

from worlds.look_outside.items import item_name_groups, num_multiple_items

from .options import PlayerGoal
from typing_extensions import NamedTuple
from worlds.look_outside.locations_consts import APT_33_LOCATIONS

can_access_roof = Has("Roof Access Key")

stairwell_planet_lock = Or(
    HasAll("Mars Disc", "Earth Disc"), HasAll("Sun Disc", "Negative Disc"))

# Perfect offering requirements
has_complete_manuscript = Has("Progressive Loose Manuscript", count=2)
has_painting = Has("Correct Painting")
has_photo = Has("Correct Photograph")
has_cctv = Has("Correct CCTV Recording")

# Any perfect offering (at least one of the four, with correct counts)
has_any_perfect_offering = Or(
    has_complete_manuscript, has_painting, has_photo, has_cctv)
# All perfect offerings (all four, with correct counts)
has_all_perfect_offerings = And(
    has_complete_manuscript, has_painting, has_photo, has_cctv)

can_open_any_simple_lock = Has("Lockpicks")  # todo: count keys
can_access_stairwell = Has("Padlock Key")
can_access_elevator = Has("Elevator Activation")
can_access_floor_2_east = can_access_stairwell
can_access_floor_2_west = can_access_elevator
can_awaken_sibyl = HasAll("Telescope", "Apt. 35 Key")
can_access_floor_1 = Or(And(can_access_floor_2_east, Has(
    "Apt. 21 Key")), can_awaken_sibyl, stairwell_planet_lock)
can_access_ground_floor = Or(can_access_elevator, And(
    can_access_stairwell, stairwell_planet_lock))
can_access_apt_21_depths = Or(And(can_access_floor_1, Has(
    "Herbicide"), Has("Jasper's Key")), can_awaken_sibyl)
can_access_basement = Or(can_access_elevator, And(
    can_access_stairwell, Has("Basement Key")))
can_access_floor_4 = can_access_elevator
can_access_metro = And(can_access_floor_4, Has("Metro Ticket"))
can_access_glitch_world = Has("Unlabeled Cartridge")
can_nestor_rafta = And(HasAll(*item_name_groups["NESTOR_QUEST_INTRO"]), can_access_floor_1, can_access_ground_floor)

can_perform_flawed_ritual = And(can_access_roof, has_any_perfect_offering)
can_perform_perfect_ritual = And(can_access_roof, has_all_perfect_offerings)
can_true_final = And(can_perform_perfect_ritual, Has("Meteor Strike"))
can_keep_promise = And(can_perform_perfect_ritual, can_awaken_sibyl)
can_reach_unity = And(can_access_apt_21_depths, Has("Small Red Key"))
can_perform_mask_ritual = And(
    can_access_roof, HasAll(*item_name_groups["MASK_OFFERING"]))

# Eternal fate = all guinea pig rituals shy of xin-amon
can_perform_eternal_fate_ritual = And(
    Has("Guinea Pig"), can_perform_flawed_ritual)
# Xin Amon ritual: all perfect offerings except CCTV, and Guinea Pig
can_perform_xin_amon_ritual = And(
    can_perform_eternal_fate_ritual, has_complete_manuscript, has_painting, has_photo)

can_words_of_power = And(
    HasAll("Book of Crossword Puzzles", "Pluto Disc"), can_access_basement)


class ExitData(NamedTuple):
    """
    Represents a one-way exit from one region to the next.
    Ability to get back to the origin location is implied and not explicitly placed.
    """
    target_region: str
    rule: Rule | None = None


class RegionData(NamedTuple):
    """Represents a region."""
    exits: dict[str, ExitData] = {}
    locations: set[str] = set()  # TODO: manage this somewhere else


f3_regions_table: dict[str, RegionData] = {
    "APT_33_HOME": RegionData(
        exits={
            "APT_33_EXIT": ExitData("FLOOR_3_HALL"),
            "APT_33_DOORWAY": ExitData("DOOR_ENCOUNTERS"),
        },
    ),
    "DOOR_ENCOUNTERS": RegionData(
        locations=set()
    ),
    "FLOOR_3_HALL": RegionData(
        exits={
            "F3_STAIRWELL_EXIT": ExitData("STAIRWELL", can_access_stairwell),
            "F3_ELEVATOR_EXIT": ExitData("ELEVATOR", can_access_elevator),
            "APT_30_DOOR": ExitData("APT_30_TAXIDERMY"),
            "APT_31_DOOR": ExitData("APT_31_STARGAZER"),
            "APT_32_DOOR": ExitData("APT_32_TEETH"),
            "APT_34_DOOR": ExitData("APT_34_FROZEN_ENTRANCE"),
            "APT_35_DOOR": ExitData("APT_35_SIBYL", Has("Apt. 35 Key")),
            "APT_36_DOOR": ExitData("APT_36_WOUNDED"),
            "APT_37_DOOR": ExitData("APT_37_VINCENT"),
            "APT_38_ROOMMATES": ExitData("APT_38_ROOMMATES"),
            "F3_JANITOR_CLOSET_DOOR": ExitData("F3_JANITOR_CLOSET", Has("Janitor Key Ring")),
        },
    ),
    "APT_30_TAXIDERMY": RegionData(exits={
        "TAXIDERMY_DOOR": ExitData("APT_30_TAXIDERMY_FLESH", Has("Shrunken Head"))}),
    "APT_30_TAXIDERMY_FLESH": RegionData(),
    "APT_31_STARGAZER": RegionData(exits={
        "GLITCH_WORLD_TV": ExitData("GLITCH_WORLD_MAIN", can_access_glitch_world)
    }),
    "GLITCH_WORLD_MAIN": RegionData(),
    "APT_32_TEETH": RegionData(exits={
        "MASTER_BEDROOM_DOOR": ExitData("APT_32_MASTER_BEDROOM_KITCHEN", Has("Door Knob"))}),
    "APT_32_MASTER_BEDROOM_KITCHEN": RegionData(),
    "APT_35_SIBYL": RegionData(),
    "APT_36_WOUNDED": RegionData(),
    "APT_37_VINCENT": RegionData(
        exits={"APT_37_LOCKED_DOOR": ExitData("APT_37_LOCKED_ROOM", can_open_any_simple_lock)}
    ),
    "APT_37_LOCKED_ROOM": RegionData(),
    "APT_38_ROOMMATES": RegionData(
        exits={
            "APT_38_KAELEY_DOOR": ExitData("APT_38_KAELEY")
        }),
    "F3_JANITOR_CLOSET": RegionData()
}

kaeley_regions_table: dict[str, RegionData] = {
    "APT_38_KAELEY": RegionData(exits={
        "KAELEY_NE_LOCK": ExitData("KAELEY_NE", can_open_any_simple_lock),
        "KAELEY_CENTER_RIGHT_LOCK1": ExitData("KAELEY_CENTER_RIGHT_TOP", can_open_any_simple_lock),
        "KAELEY_CENTER_LEFT_LOCK": ExitData("KAELEY_CENTER_LEFT", can_open_any_simple_lock),
    }),
    "KAELEY_NE": RegionData(),
    "KAELEY_E": RegionData(),
    "KAELEY_SE": RegionData(),
    "KAELEY_S": RegionData(),
    "KAELEY_CENTER_LEFT": RegionData(exits={
        "KAELEY_W_LOCK": ExitData("KAELEY_W", can_open_any_simple_lock),
        "KAELEY_SW_LOCK": ExitData("KAELEY_SW", can_open_any_simple_lock),
        "KAELEY_CENTER_HALL_LOCK_L": ExitData("KAELEY_CENTER_HALL", can_open_any_simple_lock),
    }),
    "KAELEY_CENTER_RIGHT_TOP": RegionData(exits={
        "KAELEY_CENTER_RIGHT_LOCK2": ExitData("KAELEY_CENTER_RIGHT", can_open_any_simple_lock)
    }), # this area has trickster in it
    "KAELEY_CENTER_RIGHT": RegionData(exits={
        "KAELEY_CENTER_HALL_LOCK_R": ExitData("KAELEY_CENTER_HALL", can_open_any_simple_lock),
        "KAELEY_E_LOCK": ExitData("KAELEY_E", can_open_any_simple_lock),
        "KAELEY_SE_LOCK": ExitData("KAELEY_SE", can_open_any_simple_lock),
    }),
    "KAELEY_CENTER_HALL": RegionData(exits={
        "KAELEY_CENTER_S_LOCK": ExitData("KAELEY_CENTER", can_open_any_simple_lock),
    }),
    "KAELEY_CENTER": RegionData(exits={
        "KAELEY_S_LOCK": ExitData("KAELEY_S", can_open_any_simple_lock),
    }),
    "KAELEY_SW": RegionData(),
    "KAELEY_W": RegionData(exits={
        "KAELEY_NW_LOCK": ExitData("KAELEY_NW", can_open_any_simple_lock),
    }),
    "KAELEY_NW": RegionData(),
}


# theres a total of 18 meltable blocks in apartment 34
# assumes worst case scenario: player has spent enough ice melts to go to every
# other possible location before this one
# every location has the number of ice melts increased by 1 to account for the one block in the neptune room
ice_melts_needed = {
    "APT_34_FROZEN_BEDROOM_WEST": num_multiple_items["Ice Melt Salt"] - 1,
    "APT_34_FROZEN_BEDROOM_EAST": num_multiple_items["Ice Melt Salt"],
    "APT_34_FROZEN_KITCHEN_BATHROOM_EAST": num_multiple_items["Ice Melt Salt"] - 15,
    "APT_34_FROZEN_BATHROOM_WEST": num_multiple_items["Ice Melt Salt"] - 1,
    "APT_34_FROZEN_OFFICE_NORTH": num_multiple_items["Ice Melt Salt"] - 2,
    "APT_34_FROZEN_OFFICE_SOUTH": num_multiple_items["Ice Melt Salt"] - 3,
    "APT_34_FROZEN_CLOSET": num_multiple_items["Ice Melt Salt"],
    "APT_34_FROZEN_KITCHEN_LOWER": num_multiple_items["Ice Melt Salt"] - 7,
    "APT_34_FROZEN_LONG_BEDROOM_WEST": num_multiple_items["Ice Melt Salt"] - 5,
    "APT_34_FROZEN_LONG_BEDROOM_SW": num_multiple_items["Ice Melt Salt"] - 4,
    "APT_34_FROZEN_LONG_BEDROOM_CENTER": num_multiple_items["Ice Melt Salt"] - 3,
    "APT_34_FROZEN_LONG_BEDROOM_NORTH": num_multiple_items["Ice Melt Salt"],
    "APT_34_FROZEN_LONG_BEDROOM_EAST": num_multiple_items["Ice Melt Salt"]
}

frozen_apartment_regions_table = {
    "APT_34_FROZEN_ENTRANCE": RegionData(exits={
        "ENTRANCE_EAST_ICE_BLOCK": ExitData("APT_34_FROZEN_BEDROOM_WEST", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_BEDROOM_WEST"])),
        "ENTRANCE_WEST_ICE_BLOCK": ExitData("APT_34_FROZEN_KITCHEN_BATHROOM_EAST", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_KITCHEN_BATHROOM_EAST"]))
        }
    ),
    "APT_34_FROZEN_BEDROOM_WEST": RegionData(exits={
        "BEDROOM_ICE_BLOCK": ExitData("APT_34_FROZEN_BEDROOM_EAST", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_BEDROOM_EAST"]))
        }
    ),
    "APT_34_FROZEN_BEDROOM_EAST": RegionData(),
    "APT_34_FROZEN_KITCHEN_BATHROOM_EAST": RegionData(exits={
        "BATHROOM_ICE_BLOCK_EAST_SIDE": ExitData("APT_34_FROZEN_BATHROOM_WEST", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_BATHROOM_WEST"])),
        "KITCHEN_ICE_BLOCK": ExitData("APT_34_FROZEN_KITCHEN_LOWER", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_KITCHEN_LOWER"]))
    }),
    "APT_34_FROZEN_BATHROOM_WEST": RegionData(
        exits={
            "BATHROOM_ICE_BLOCK_WEST_SIDE": ExitData("APT_34_FROZEN_KITCHEN_BATHROOM_EAST", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_KITCHEN_BATHROOM_EAST"])),
            "BATHROOM_ICE_BLOCK_SOUTH": ExitData("APT_34_FROZEN_OFFICE_NORTH", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_OFFICE_NORTH"]))
        }
    ),
    "APT_34_FROZEN_OFFICE_NORTH": RegionData(
        exits={
            "OFFICE_ICE_BLOCK_NORTH": ExitData("APT_34_FROZEN_BATHROOM_WEST", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_BATHROOM_WEST"])),
            "OFFICE_ICE_BLOCK_CENTER": ExitData("APT_34_FROZEN_OFFICE_SOUTH", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_OFFICE_SOUTH"]))
        }),
    "APT_34_FROZEN_OFFICE_SOUTH": RegionData(
        exits={
            "OFFICE_ICE_BLOCK_SOUTH": ExitData("APT_34_FROZEN_CLOSET", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_CLOSET"])),
            "OFFICE_ICE_BLOCK_KITCHEN": ExitData("APT_34_FROZEN_KITCHEN_LOWER", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_KITCHEN_LOWER"])),
        }),
    "APT_34_FROZEN_KITCHEN_LOWER": RegionData(exits={
        "KITCHEN_ICE_BLOCK_OFFICE": ExitData("APT_34_FROZEN_OFFICE_SOUTH", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_OFFICE_SOUTH"])),
        "KITCHEN_ICE_BLOCK_LONG_BEDROOM": ExitData("APT_34_FROZEN_LONG_BEDROOM_WEST", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_LONG_BEDROOM_WEST"]))
    }),
    "APT_34_FROZEN_LONG_BEDROOM_WEST": RegionData(exits={
        "LONG_BEDROOM_ICE_BLOCK_WEST": ExitData("APT_34_FROZEN_LONG_BEDROOM_SW", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_LONG_BEDROOM_SW"])),
    }),
    "APT_34_FROZEN_LONG_BEDROOM_SW": RegionData(exits={
        "LONG_BEDROOM_SW_ICE_BLOCK_C": ExitData("APT_34_FROZEN_LONG_BEDROOM_CENTER", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_LONG_BEDROOM_CENTER"])),
    }),
    "APT_34_FROZEN_LONG_BEDROOM_CENTER": RegionData(exits={
        "LONG_BEDROOM_CENTER_ICE_BLOCK_N": ExitData("APT_34_FROZEN_LONG_BEDROOM_NORTH", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_LONG_BEDROOM_NORTH"])),
        "LONG_BEDROOM_CENTER_ICE_BLOCK_E": ExitData("APT_34_FROZEN_LONG_BEDROOM_EAST", Has("Ice Melt Salt", count=ice_melts_needed["APT_34_FROZEN_LONG_BEDROOM_EAST"])),
    }),
    "APT_34_FROZEN_LONG_BEDROOM_NORTH": RegionData(),
    "APT_34_FROZEN_LONG_BEDROOM_EAST": RegionData(),
    "APT_34_FROZEN_CLOSET": RegionData(),
}

f2_west_regions_table = {
    "FLOOR_2_WEST": RegionData(exits={
        "APT_25_DOOR": ExitData("APT_25_DAN", Has("Dan")),
        "APT_27_DOOR": ExitData("APT_27_TYPEWRITHER"),
        "APT_28_DOOR": ExitData("APT_28_FLOODED_ENTRYWAY"),
    }),
    "APT_25_DAN": RegionData(),
    "APT_27_TYPEWRITHER": RegionData(),
    "APT_28_FLOODED_ENTRYWAY": RegionData()
}

f2_east_regions_table = {
    "FLOOR_2_EAST": RegionData(exits={
        "APT_20_DOOR": ExitData("APT_20_JEANNE"),
        "APT_20_DOOR_HYDRA": ExitData("APT_20_JEANNE_HYDRA", can_access_ground_floor),
        "APT_21_DOOR": ExitData("APT_21_LYLE", Has("Apt. 21 Key")),
        "APT_22_DOOR": ExitData("APT_22_HARRIET"),
        "LEIGHS_APARTMENT_DOOR": ExitData("LEIGHS_APARTMENT"),  
        "LEIGHS_APARTMENT_QUEST_DOOR": ExitData("LEIGHS_APARTMENT_QUEST" , And(Has("Leigh"), Has("Cellphone"))),
        "APT_24_DOOR": ExitData("APT_24_EUGENE")
    }),
    "APT_20_JEANNE": RegionData(),
    "APT_20_JEANNE_HYDRA": RegionData(),
    "APT_21_LYLE": RegionData(exits={"LYLE_BATHROOM_F1_CONNECTION": ExitData("FLOOR_1_MAZE")}),
    "APT_22_HARRIET": RegionData(),
    "LEIGHS_APARTMENT": RegionData(),
    "LEIGHS_APARTMENT_QUEST": RegionData(),
    "APT_24_EUGENE": RegionData(),
}

f1_regions_table: dict[str, RegionData] = {
    "FLOOR_1_MAZE": RegionData(
        exits={
            "F1_ELEVATOR_EXIT": ExitData("ELEVATOR", can_access_elevator),
            "FRED_APARTMENT_DOOR": ExitData("FRED_APARTMENT"),
            # same for here, is rat hell activated by f1
            "RAT_HELL_ENTRANCE": ExitData("RAT_HELL", can_access_floor_1),
        }
    ),
    "FRED_APARTMENT": RegionData(),
    "RAT_HELL": RegionData()
}

basement_regions_table: dict[str, RegionData] = {
    "BASEMENT_HALL": RegionData()
}

ground_regions_table: dict[str, RegionData] = {
    "GROUND_FLOOR_WEST": RegionData(
        exits={}),
    "GROUND_FLOOR_EAST": RegionData(
        exits={})
}

misc_regions_table: dict[str, RegionData] = {
    "STAIRWELL": RegionData(
        exits={
            "ROOF_DOOR": ExitData("ROOF", can_access_roof),
            #"FLOOR_2_STAIRWELL_DOOR": ExitData("FLOOR_2_EAST"),
            # floor 1 is skipped here since it unlocks from the other side
            #"GROUND_FLOOR_STAIRWELL_DOOR": ExitData("GROUND_FLOOR_EAST", stairwell_planet_lock),
            #"BASEMENT_STAIRWELL_DOOR": ExitData("BASEMENT_HALL", Has("Basement Key")),
        }
    ),
    "ROOF": RegionData(
        exits={}
    ),
    "ELEVATOR": RegionData(
        exits={
            "ELEVATOR_FLOOR_3_EXIT": ExitData("FLOOR_3_HALL", can_access_elevator),
            #"ELEVATOR_FLOOR_2_EXIT": ExitData("FLOOR_2_WEST", can_access_elevator),
            #"ELEVATOR_FLOOR_1_EXIT": ExitData("FLOOR_1_MAZE", can_access_elevator),
            #"ELEVATOR_GROUND_FLOOR_EXIT": ExitData("GROUND_FLOOR_WEST", can_access_elevator),
        }
    )

}

all_regions_table = {
    **misc_regions_table,
    **f3_regions_table,
    **frozen_apartment_regions_table,
    **kaeley_regions_table,
    #**f2_east_regions_table,
}

"""
LEAVING THESE OUT AND TESTING WITH F3 FOR NOW:

**f2_regions_table,
    **f1_regions_table,
    **ground_regions_table,
    **basement_regions_table
"""
