from test.general import setup_multiworld, setup_solo_multiworld

from worlds.look_outside import LookOutsideWorld
from worlds.look_outside.items_consts import num_multiple_items
from worlds.look_outside.options import IncludeArms, StartingGames
from worlds.look_outside.test.bases import LOTestBase

class TestOptionsPrecollectedNotInPool(LOTestBase):
    options = {
        "starting_games": StartingGames.option_vanilla,
        "include_arms": IncludeArms.option_start_with_both_arms
    }

    def test_precollected_games(self):        
        game_names = {"Super Jumplad", "Madwheels 97", "Myrmidon"}
        precollected_names = {item.name for item in self.multiworld.precollected_items[self.player]}
        itempool_names = {item.name for item in self.multiworld.itempool}

        self.assertTrue(
            game_names.issubset(precollected_names),
            f"Expected vanilla starting games to be precollected, got: {precollected_names}"
        )

        for game in game_names:
            self.assertNotIn(
                game,
                itempool_names,
                f"{game} should be precollected and not also present in the item pool"
            )

    def test_precollected_arms(self):
        arm_names = {"Player's Left Arm", "Player's Right Arm"}
        itempool_names = {item.name for item in self.multiworld.itempool}

        for arm in arm_names:
            self.assertNotIn(
                arm,
                itempool_names,
                f"{arm} should be precollected and not also present in the item pool"
            )
    
class TestRegularPrecollectedNotInPool(LOTestBase):

    def test_multiple_item(self):
        self.assertEqual(
            len(self.multiworld.worlds),
            1,
            "working with a solo world"
        )

        progressive_name = "Progressive Rat Child"
        breakable_key_name = "Iris Key"
        currency_name = "Worm Egg"
        ammo_name = "3x Rifle Bullets"

        self.assertEqual(
            sum(1 for item in self.multiworld.itempool if item.name == progressive_name),
            num_multiple_items[progressive_name],
            "progressive items should have count from the table"
        )

        self.assertEqual(
            sum(1 for item in self.multiworld.itempool if item.name == breakable_key_name),
            num_multiple_items[breakable_key_name],
            "breakable keys should have count from the table"
        )

        self.assertEqual(
            sum(1 for item in self.multiworld.itempool if item.name == currency_name),
            num_multiple_items[currency_name],
            "unique currency should have count from the table"
        )

        self.assertEqual(
            sum(1 for item in self.multiworld.itempool if item.name == ammo_name),
            num_multiple_items[ammo_name],
            "Precollected ammo should have count from the table"
        )


    def test_precollected_multiple_item(self):
        multiworld = setup_solo_multiworld(LookOutsideWorld, steps=("generate_early","create_regions"))
        world = multiworld.worlds[1]

        self.assertEqual(
            len(multiworld.worlds),
            1,
            "working with a solo world"
        )

        progressive_name = "Progressive Rat Child"
        breakable_key_name = "Iris Key"
        currency_name = "Worm Egg"
        ammo_name = "3x Rifle Bullets"

        multiworld.push_precollected(world.create_item(progressive_name))

        multiworld.push_precollected(world.create_item(breakable_key_name))
        multiworld.push_precollected(world.create_item(breakable_key_name))

        multiworld.push_precollected(world.create_item(currency_name))

        multiworld.push_precollected(world.create_item(ammo_name))

        world.create_items()

        self.assertEqual(
            sum(1 for item in multiworld.itempool if item.name == progressive_name),
            num_multiple_items[progressive_name] - 1,
            "precollected progressive item should reduce count in the pool by 1"
        )

        self.assertEqual(
            sum(1 for item in multiworld.itempool if item.name == breakable_key_name),
            num_multiple_items[breakable_key_name] - 2,
            "2 precollected breakable keys should reduce count in the pool by 2"
        )

        self.assertEqual(
            sum(1 for item in multiworld.itempool if item.name == currency_name),
            num_multiple_items[currency_name] - 1,
            "Precollected unique currency should reduce count in the pool by 1"
        )

        self.assertEqual(
            sum(1 for item in multiworld.itempool if item.name == ammo_name),
            num_multiple_items[ammo_name] - 1,
            "Precollected ammo should reduce count in the pool by 1"
        )

    def test_precollected_unique_item(self):
        multiworld = setup_solo_multiworld(LookOutsideWorld, steps=("generate_early","create_regions"))
        world = multiworld.worlds[1]
        precollected_item = world.create_item("Joel")
        multiworld.push_precollected(precollected_item)
        world.create_items()

        self.assertEqual(
            sum(1 for item in multiworld.itempool if item.name == "Joel"),
            0,
            "Precollected unique items should not appear in the item pool"
        )

    def test_precollected_filler(self):
        multiworld = setup_solo_multiworld(LookOutsideWorld, steps=("generate_early","create_regions"), seed=1)
        world = multiworld.worlds[1]
        precollected_item = world.create_item("Tonic")
        multiworld.push_precollected(precollected_item)
        world.create_items()

        self.assertGreaterEqual(
            sum(1 for item in multiworld.itempool if item.name == "Tonic"),
            1,
            "Precollected filler items should still appear in the item pool"
        )

class TestItemPoolInMultiworld(LOTestBase):

    def test_two_lo_world_item_count(self):
        multiworld = setup_multiworld(
            [LookOutsideWorld, LookOutsideWorld],
            steps=("generate_early", "create_regions", "create_items")
        )

        self.assertEqual(
            sum(1 for item in multiworld.itempool if item.player == 1),
            sum(1 for item in multiworld.itempool if item.player == 2),
            "A two-player Look Outside multiworld with equal location counts should contain equal number of items for both worlds"
        )

