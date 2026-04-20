import settings
import typing

from worlds.look_outside.items import ItemCat, ItemTag, item_table, get_item_id, item_name_groups
from .locations import get_location_id, location_table

from .options import LookOutsideOptions  # the options we defined earlier
from worlds.AutoWorld import World
from BaseClasses import Item, ItemClassification
from rule_builder.cached_world import CachedRuleBuilderWorld
from worlds.look_outside.regions import create_and_connect_regions
from worlds.look_outside.rules import set_all_rules
from worlds.look_outside.locations import create_all_locations
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

    origin_region_name = "APT_33"

    item_name_to_id = {name: get_item_id(item_table[name]) for name in item_table}
    location_name_to_id = {name: get_location_id(location_table[name]) for name in location_table}

    web = LookOutsideWebworld()

    def create_regions(self) -> None:
        create_and_connect_regions(self)
        create_all_locations(self)

    def create_item(self, item: str) -> LOItem:
        classification = ItemClassification.filler
        item_info = item_table[item]
        if item_info.category == ItemCat.SKILL:
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

        self.multiworld.itempool += [self.create_item(item) for item in ["Testsword", "Roof Access Key", "Padlock Key"]]


    def set_rules(self) -> None:
        set_all_rules(self)

    def fill_slot_data(self) -> dict[str, any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "goal", "include_arms", "friendly_fire", "rusty_crown", "include_test_gear", "include_nestor_quest", 
            "include_shades", "include_mask", "include_roommate_quests", "lockpicks_in_logic", "starting_games", 
            "death_link"
        )

# for debugging purposes, you may want to visualize the layout of your world. Uncomment the following code to
# write a PlantUML diagram to the file "my_world.puml" that can help you see whether your regions and locations
# are connected and placed as desired
# from Utils import visualize_regions
# visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")