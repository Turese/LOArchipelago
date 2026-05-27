from __future__ import annotations

from typing import TYPE_CHECKING

from worlds.look_outside.options import StartingGames, IncludeArms,\
    LookOutsideOptions, PlayerGoal

from worlds.look_outside.items_consts import ItemCat, ItemTag, item_table, item_name_groups,\
    num_multiple_items, LOItem

from BaseClasses import ItemClassification

if TYPE_CHECKING:
    from .__init__ import LookOutsideWorld

def check_gate_classification_by_options(item: str, options: LookOutsideOptions) -> ItemClassification:
    if item == "Rusty Crown":
        if options.rusty_crown:
            return ItemClassification.progression
        else:
            return ItemClassification.useful
    if item in item_name_groups["QUEST_ROOMMATES"]:
        if options.include_roommate_quests:
            return ItemClassification.progression
        else:
            return ItemClassification.useful
    if item in item_name_groups["USEFUL_SKILL_VIDEO_GAME"]:
        if options.include_game_skills:
            return ItemClassification.progression
    if options.include_mask:
        if item == "Honko's Grand Journey": # needed to fight honko
            return ItemClassification.progression
    if options.allow_killing_shopkeepers:
        if item in item_name_groups["SHOPKEEPER_PROGRESSION_CASH"]:
            return ItemClassification.useful
        else:
            return ItemClassification.progression
    if options.goal in { PlayerGoal.option_all_roof_endings, PlayerGoal.option_all_endings, PlayerGoal.option_true_final }:
        if item == "Skill: Meteor Strike":
            return ItemClassification.progression
    else:
        if item == "Skill: Meteor Strike":
            return ItemClassification.filler
    return ItemClassification.progression

def create_lo_item(world: LookOutsideWorld, item: str) -> LOItem:
    classification = ItemClassification.filler
    item_info = item_table[item]

    if ItemTag.CHECK_GATE in item_info.tags or ItemTag.BREAKABLE_KEY in item_info.tags or ItemTag.OFFERING in item_info.tags or ItemTag.SPECIAL_CURRENCY in item_info.tags:
        classification = check_gate_classification_by_options(item, world.options)
    elif item_info.category == ItemCat.SKILL:
        classification = ItemClassification.useful
    elif item_info.category == ItemCat.MISC:
        classification = ItemClassification.useful
    elif ItemTag.USEFUL in item_info.tags:
        classification = ItemClassification.useful
    elif item_info.category == ItemCat.TRAP:
        classification = ItemClassification.trap
    return LOItem(item, classification, world.item_name_to_id[item], world.player)
    
def create_all_items(world: LookOutsideWorld):
    # Add items to the Multiworld.
        # If there are two of the same item, the item has to be twice in the pool.
        # Which items are added to the pool may depend on player options, e.g. custom win condition like triforce hunt.
        # Having an item in the start inventory won't remove it from the pool.
        # If you want to do that, use start_inventory_from_pool

        # TODO: IMPLEMENT WITH LOGIC

        mandatory_items = []
        unique_items = []
        remaining_items = []

        excluded_items = set()

        precollect_games(world)
        precollect_arms(world)

        if not world.options.include_nestor_quest:
            for item in item_name_groups["NESTOR_QUEST_INTRO"]:
                excluded_items.add(item)

        if not world.options.include_test_gear:
            for item in item_name_groups["BROKEN_TEST_ITEM"]:
                excluded_items.add(item)

        if not world.options.include_mask:
            for item in item_name_groups["MASK_AREA_ENTRY"]:
                excluded_items.add(item)

        if not world.options.include_game_skills:
            excluded_items.update(item_name_groups["VIDEO_GAME_SKILL"])

        if not world.options.include_roommate_quests:
            excluded_items.add("Cell Phone")

        for item in world.multiworld.precollected_items[world.player]:
            if ItemTag.UNIQUE in item_table[item.name].tags:
                excluded_items.add(item.name)

        for item_name, item_info in item_table.items():
            if item_name in excluded_items:
                continue
            category = item_info.category
            tags = item_info.tags
            if ItemTag.PROGRESSIVE in tags or ItemTag.BREAKABLE_KEY in tags or ItemTag.AMMO in tags or ItemTag.SPECIAL_CURRENCY in tags:
                mandatory_items += [item_name] * num_multiple_items[item_name]
            elif category == ItemCat.SKILL or category == ItemCat.MISC:
                mandatory_items += [item_name]
            # todo: clean up redundant tags. all offerings besides the progressive one are already both unique and check gates
            elif ItemTag.UNIQUE in tags or ItemTag.CHECK_GATE in tags or ItemTag.OFFERING in tags:
                unique_items += [item_name]
            else:
                remaining_items += [item_name]
        
        for item in mandatory_items:
            world.multiworld.itempool += [create_lo_item(world, item)]

        for item in unique_items:
            world.multiworld.itempool += [create_lo_item(world, item)]

        num_locations = len(world.multiworld.get_unfilled_locations())
        num_itempool = len(world.multiworld.itempool)
    
        slots_to_fill = num_locations - num_itempool

        for i in range(slots_to_fill):
            filler_item = remaining_items[i % len(remaining_items)]
            world.multiworld.itempool += [create_lo_item(world, filler_item)]

        print(f"Added {len(world.multiworld.itempool)} items to the pool, filling {slots_to_fill} slots with filler items.")


# yaml option for starting games
def precollect_games(world: LookOutsideWorld):
    game_option = world.options.starting_games
    if game_option == StartingGames.option_vanilla:
        world.multiworld.push_precollected(create_lo_item(world, "Super Jumplad"))
        world.multiworld.push_precollected(create_lo_item(world, "Madwheels 97"))
        world.multiworld.push_precollected(create_lo_item(world, "Myrmidon"))
    if game_option == StartingGames.option_random_3:
        game_list = list(item_name_groups["VIDEO_GAME"])
        world.multiworld.random.shuffle(game_list)
        for game in game_list[:4]:
            world.multiworld.push_precollected(create_lo_item(world, game))

# yaml option for starting arms
def precollect_arms(world: LookOutsideWorld):
    arms_option = world.options.include_arms
    if arms_option == IncludeArms.option_start_with_both_arms:
        world.multiworld.push_precollected(create_lo_item(world, "Player's Left Arm"))
        world.multiworld.push_precollected(create_lo_item(world, "Player's Right Arm"))
    elif arms_option == IncludeArms.option_start_with_left_arm:
        world.multiworld.push_precollected(create_lo_item(world, "Player's Left Arm"))
    elif arms_option == IncludeArms.option_start_with_right_arm:
        world.multiworld.push_precollected(create_lo_item(world, "Player's Right Arm"))
