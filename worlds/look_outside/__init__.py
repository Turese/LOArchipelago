import settings
import typing

from worlds.look_outside.items_consts import ItemCat, ItemTag, item_table, get_item_id, item_name_groups,\
    num_multiple_items, LOItem
from .locations import get_location_id, get_location_name, location_table, create_all_locations

from .options import LookOutsideOptions  # the options we defined earlier
from worlds.AutoWorld import World
from BaseClasses import ItemClassification
from rule_builder.cached_world import CachedRuleBuilderWorld
from worlds.look_outside.regions import create_and_connect_regions
from worlds.look_outside.rules import set_all_rules
from worlds.look_outside.web_world import LookOutsideWebworld

from worlds.look_outside.items import create_all_items, create_lo_item

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
    location_name_to_id = {get_location_name(location_str_id, False): get_location_id(location_table[location_str_id]) for location_str_id, n in location_table.items()}

    web = LookOutsideWebworld()

    def create_regions(self) -> None:
        create_and_connect_regions(self)
        create_all_locations(self)
        # TEST CODE FOR REGION MAPPING
        from Utils import visualize_regions
        visualize_regions(self.multiworld.get_region("APT_33_HOME", self.player), "my_world.puml")

    def create_item(self, item: str) -> LOItem:
        return create_lo_item(self, item)

    def create_event(self, event: str) -> LOItem:
        return LOItem(event, ItemClassification.progression, None, self.player)
    
    def create_items(self) -> None:
        create_all_items(self)  

    def set_rules(self) -> None:
        set_all_rules(self)

    def fill_slot_data(self) -> dict[str, any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "goal", "include_arms", "friendly_fire", "rusty_crown", "include_test_gear", "include_nestor_quest", 
            "include_shades", "include_mask", "include_roommate_quests", "starting_games", 
            "death_link"
        )