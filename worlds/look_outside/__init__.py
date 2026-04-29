from MultiServer import console
import settings
import typing

from worlds.look_outside.items import ItemCat, ItemTag, item_table, get_item_id, item_name_groups,\
    num_multiple_items
from .locations import get_location_id, get_location_name, location_table, create_all_locations

from .options import LookOutsideOptions  # the options we defined earlier
from worlds.AutoWorld import World
from BaseClasses import Item, ItemClassification
from rule_builder.cached_world import CachedRuleBuilderWorld
from worlds.look_outside.regions import create_and_connect_regions
from worlds.look_outside.rules import set_all_rules
from worlds.look_outside.web_world import LookOutsideWebworld


class LOItem(Item):  # or from Items import MyGameItem
    game = "Look Outside"


class LOSettings(settings.Group):
    pass


class LookOutsideWorld(CachedRuleBuilderWorld):
    """Look Outside is a survival horror RPG set in a single apartment building.
    A mysterious event turns anyone who looks out the window into grotesque monsters,
    leaving the world in absolute chaos. Scavenge the building to seek food, supplies,
    and weapons while encountering strange characters - human and otherwise."""
    game = "Look Outside"  # name of the game/world
    options_dataclass = LookOutsideOptions  # options the player can set
    options: LookOutsideOptions  # typing hints for option results
    settings: typing.ClassVar[LOSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    item_name_groups = item_name_groups

    origin_region_name = "APT_33_HOME"

    item_name_to_id = {name: get_item_id(item_table[name]) for name in item_table}
    location_name_to_id = {get_location_name(location_table[location_str_id], False): get_location_id(location_table[location_str_id]) for location_str_id, n in location_table.items()}

    web = LookOutsideWebworld()

    def create_regions(self) -> None:
        create_and_connect_regions(self)
        create_all_locations(self)
        # TEST CODE FOR REGION MAPPING
        from Utils import visualize_regions
        visualize_regions(self.multiworld.get_region("APT_33_HOME", self.player), "my_world.puml")

    def create_item(self, item: str) -> LOItem:
        classification = ItemClassification.filler
        item_info = item_table[item]
        if item_info.category == ItemCat.SKILL:
            classification = ItemClassification.useful
        if item_info.category == ItemCat.RECRUIT:
            classification = ItemClassification.useful
        if ItemTag.CHECK_GATE in item_info.tags:
            classification = ItemClassification.progression
        if ItemTag.USEFUL in item_info.tags:
            classification = ItemClassification.useful
        return LOItem(item, classification, self.item_name_to_id[item], self.player)

    def create_event(self, event: str) -> LOItem:
        return LOItem(event, ItemClassification.progression, None, self.player)
    
    def create_items(self) -> None:
        # Add items to the Multiworld.
        # If there are two of the same item, the item has to be twice in the pool.
        # Which items are added to the pool may depend on player options, e.g. custom win condition like triforce hunt.
        # Having an item in the start inventory won't remove it from the pool.
        # If you want to do that, use start_inventory_from_pool

        # TODO: IMPLEMENT WITH LOGIC

        mandatory_items = []
        unique_items = []
        remaining_items = []
        excluded_items = {"Simple Key", "Iris Key"}

        for item_name, item_info in item_table.items():
            if item_name in excluded_items:
                continue
            category = item_info.category
            tags = item_info.tags
            if ItemTag.PROGRESSIVE in tags or ItemTag.BREAKABLE_KEY in tags:
                mandatory_items += [item_name] * num_multiple_items[item_name]
            if category in {ItemCat.SKILL, ItemCat.RECRUIT, ItemCat.MISC}:
                mandatory_items.append(item_name)
            elif ItemTag.UNIQUE in tags:
                unique_items.append(item_name)
            elif ItemTag.CHECK_GATE in tags:
                mandatory_items.append(item_name)
            else:
                remaining_items.append(item_name)
        
        for item in mandatory_items:
            self.multiworld.itempool += [self.create_item(item)]

        for item in unique_items:
            self.multiworld.itempool += [self.create_item(item)]

        num_locations = len(self.multiworld.get_unfilled_locations())
        num_itempool = len(self.multiworld.itempool)
        print('***difference between num regions and num items: ' + str(num_locations - num_itempool))
    
        slots_to_fill = num_locations - num_itempool

        self.random.shuffle(remaining_items)

        for i in range(slots_to_fill):
            filler_item = remaining_items[i % len(remaining_items)]
            self.multiworld.itempool += [self.create_item(filler_item)]

        # todo: bring in filler items; floor 3 doesnt have enough locations for everything       

    def set_rules(self) -> None:
        set_all_rules(self)

    def fill_slot_data(self) -> dict[str, any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "goal", "include_arms", "friendly_fire", "rusty_crown", "include_test_gear", "include_nestor_quest", 
            "include_shades", "include_mask", "include_roommate_quests", "lockpicks_in_logic", "starting_games", 
            "death_link"
        )