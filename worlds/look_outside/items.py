from __future__ import annotations

from typing import TYPE_CHECKING

from worlds.look_outside.options import LookOutsideOptions, StartingGames, IncludeArms

from worlds.look_outside.items_consts import ItemCat, ItemTag, item_table, get_item_id, item_name_groups,\
    num_multiple_items, LOItem

from BaseClasses import ItemClassification

if TYPE_CHECKING:
    from .__init__ import LookOutsideWorld

def create_lo_item(world: LookOutsideWorld, item: str) -> LOItem:
    classification = ItemClassification.filler
    item_info = item_table[item]
    
    if (item == "Rusty Crown" and world.options.rusty_crown == 0): 
        classification = ItemClassification.useful
    if (world.options.include_roommate_quests == 0 and item in item_name_groups["QUEST_ROOMMATES"]):
        classification = ItemClassification.useful
    if (world.options.include_roommate_quests == 0 and item == "Cell Phone"):
        classification = ItemClassification.filler
    elif ItemTag.CHECK_GATE in item_info.tags or ItemTag.BREAKABLE_KEY in item_info.tags or ItemTag.OFFERING in item_info.tags:
        classification = ItemClassification.progression
    elif item_info.category == ItemCat.SKILL:
        classification = ItemClassification.useful
    elif item_info.category == ItemCat.MISC:
        classification = ItemClassification.useful
    elif ItemTag.USEFUL in item_info.tags:
        classification = ItemClassification.useful
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

        # todo: bring these back
        excluded_items = {"Simple Key", "Iris Key"}

        precollect_games(world)
        precollect_arms(world)

        if world.options.include_nestor_quest == 0:
            for item in item_name_groups["NESTOR_QUEST_INTRO"]:
                excluded_items.add(item)

        if world.options.include_test_gear == 0:
            for item in item_name_groups["BROKEN_TEST_ITEM"]:
                excluded_items.add(item)

        if world.options.include_mask == 0:
            for item in item_name_groups["MASK_AREA_ENTRY"]:
                excluded_items.add(item)

        for item in world.multiworld.precollected_items[world.player]:
            excluded_items.add(item.name)

        for item_name, item_info in item_table.items():
            if item_name in excluded_items:
                continue
            category = item_info.category
            tags = item_info.tags
            if ItemTag.PROGRESSIVE in tags or ItemTag.BREAKABLE_KEY in tags:
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
        for game in game_list[:3]:
            world.multiworld.push_precollected(create_lo_item(world, game))

# yaml option for starting arms
def precollect_arms(world: LookOutsideWorld):
    arms_option = world.options.include_arms
    if arms_option == IncludeArms.option_start_armed:
        world.multiworld.push_precollected(create_lo_item(world, "Player's Left Arm"))
        world.multiworld.push_precollected(create_lo_item(world, "Player's Right Arm"))
    elif arms_option == IncludeArms.option_start_left:
        world.multiworld.push_precollected(create_lo_item(world, "Player's Left Arm"))
    elif arms_option == IncludeArms.option_start_right:
        world.multiworld.push_precollected(create_lo_item(world, "Player's Right Arm"))
