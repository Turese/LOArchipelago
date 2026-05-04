from rule_builder.rules import Has, HasAll, Or, And, HasAny

from worlds.look_outside.items import item_name_groups, num_multiple_items

# Perfect offering requirements
turned_in_complete_manuscript = And(Has("Progressive Loose Manuscript", count=2), Has("MET_JASPER"))
turned_in_painting = HasAll("Correct Painting", "MET_AURELIUS")
turned_in_photo = HasAll("Correct Photograph", "MET_ASTER")
turned_in_cctv = HasAll("Correct CCTV Recording", "MET_BERYL")

# Any perfect offering (at least one of the four, with correct counts)
has_any_perfect_offering = Or(
    turned_in_complete_manuscript, turned_in_painting, turned_in_photo, turned_in_cctv)
# All perfect offerings (all four, with correct counts)
has_all_perfect_offerings = And(
    turned_in_complete_manuscript, turned_in_painting, turned_in_photo, turned_in_cctv)

can_open_any_simple_lock = Has("Lockpicks")  # todo: count keys
can_access_stairwell = Has("Padlock Key")

can_clear_with_herbicide = Has("Herbicide", count=num_multiple_items["Herbicide"])
can_clear_with_sapper_charge = Has("Sapper Charge", count=num_multiple_items["Sapper Charge"])

met_all_astronomers = HasAll("MET_ASTER", "MET_JASPER", "MET_AURELIUS", "MET_BERYL")

can_access_elevator = Has("Elevator Activation")
can_access_floor_2_east = can_access_stairwell
can_access_floor_2_west = can_access_elevator
can_access_basement = Or(can_access_elevator, And(
    can_access_stairwell, Has("Basement Key")))
can_access_floor_4 = can_access_elevator
can_access_metro = And(can_access_floor_4, Has("Metro Ticket"))
can_nestor_rafta = And(HasAll(*item_name_groups["NESTOR_QUEST_INTRO"]), Has("MET_RAFTA"), Has("MET_NESTOR"))
can_leigh_quest = And(Has("Leigh"), Has("Phone"))

can_perform_flawed_ritual = has_any_perfect_offering
can_perform_perfect_ritual = has_all_perfect_offerings
can_true_final = And(can_perform_perfect_ritual, Has("Meteor Strike"))
can_keep_promise = And(can_perform_perfect_ritual, Has("AWAKENED_SIBYL"))
can_perform_mask_ritual = And(HasAll(*item_name_groups["MASK_OFFERING"]), met_all_astronomers)

# Eternal fate = all guinea pig rituals shy of xin-amon
can_perform_eternal_fate_ritual = And(
    Has("Guinea Pig"), 
    HasAny("MET_ASTER", "MET_JASPER", "MET_AURELIUS", "MET_BERYL")
)
# Xin Amon ritual: all perfect offerings except CCTV, and Guinea Pig
can_perform_xin_amon_ritual = And(
    can_perform_eternal_fate_ritual, turned_in_complete_manuscript, turned_in_painting, turned_in_photo, Has("MET_BERYL"))

can_words_of_power = And(
    HasAll("Book of Crossword Puzzles", "Pluto Disc"), can_access_basement)
