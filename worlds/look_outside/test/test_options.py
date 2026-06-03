from BaseClasses import ItemClassification
from worlds.look_outside.locations import exclude_locations
from worlds.look_outside.locations_consts import location_name_groups, location_table
from worlds.look_outside.items_consts import item_name_groups

from worlds.look_outside.options import IncludeShades, PlayerGoal, StartingGames
from worlds.look_outside.test.bases import LOTestBase

class AllLocationOptionsTest(LOTestBase):
    options = {
        "goal": PlayerGoal.option_all_endings,
        "friendly_fire": True,
        "allow_killing_shopkeepers": True,
        "include_roommate_quests": True,
        "randomize_door_encounters": True,
        "include_mask": True,
        "rat_friendly_fire": True,
        "include_shades": IncludeShades.option_large_shades_and_spider_and_crawling_shade,
        "include_nestor_quest": True,
        "rusty_crown": True,
        "include_game_skills": True
    }

    def test_all_locations_included(self):
        all_location_names = {location.name for location in self.multiworld.get_locations()}
        expected_location_names = set(location_table[location_id].str_name for location_id in location_table.keys()) - exclude_locations(self.world)
        
        location_difference = expected_location_names - all_location_names
        self.assertTrue(
            len(location_difference) == 0,
            f"Locations should not be missing when all options are enabled: {sorted(location_difference)}"
        )

class FriendlyFireExcluded(LOTestBase):
    options = {
        "friendly_fire": False,
        "include_roommate_quests": True,
        "randomize_door_encounters": True,
        "include_mask": True
    }

    def test_friendly_fire_locations_are_excluded_when_disabled(self):
        friendly_fire_names = {
            location_table[location_id].str_name
            for location_id in location_name_groups["FRIENDLY_FIRE"]
        }
        existing_location_names = {location.name for location in self.multiworld.get_locations()}

        excluded_locations = friendly_fire_names & existing_location_names
        self.assertTrue(
            len(excluded_locations) == 0,
            f"Friendly fire locations should not be created when friendly fire is disabled: {sorted(excluded_locations)}"
        )

class FriendlyFireIncluded(LOTestBase):
    options = {
        "friendly_fire": True,
        "allow_killing_shopkeepers": True,
        "include_roommate_quests": True,
        "randomize_door_encounters": True,
        "include_mask": True
    }

    def test_friendly_fire_locations_are_included_when_enabled(self):
        friendly_fire_names = {
            location_table[location_id].str_name
            for location_id in location_name_groups["FRIENDLY_FIRE"]
        }
        existing_location_names = {location.name for location in self.multiworld.get_locations()}

        excluded_locations = friendly_fire_names & existing_location_names
        self.assertTrue(len(excluded_locations) == len(friendly_fire_names),
            f"M{sorted(friendly_fire_names - excluded_locations)}"  
        )

class ShopKeeperFriendlyFire(LOTestBase):
    options = {
        "friendly_fire": True,
        "allow_killing_shopkeepers": False,
        "include_roommate_quests": True,
        "randomize_door_encounters": True,
        "include_mask": True,
        "rat_friendly_fire": True,
        "include_shades": IncludeShades.option_large_shades_and_spider_and_crawling_shade,
        "include_nestor_quest": True,
        "rusty_crown": True,
        "include_game_skills": True
    }

    def test_shopkeeper_locations_are_excluded_when_disabled(self):
        existing_location_names = {location.name for location in self.multiworld.get_locations()}

        friendly_fire_names = {
            location_table[location_id].str_name
            for location_id in location_name_groups["FRIENDLY_FIRE"]
        }

        killed_mutt_id = "MUTT_COMBAT_VICTORY"
        killed_eugene_id = "APT_24_EUGENE_COMBAT_VICTORY"

        killed_mutt_name = location_table[killed_mutt_id].str_name
        killed_eugene_name = location_table[killed_eugene_id].str_name

        locations_to_exclude_set = exclude_locations(self.world)

        self.assertTrue(
            killed_mutt_id in locations_to_exclude_set and killed_eugene_id in locations_to_exclude_set,
            f" {locations_to_exclude_set}; Exclude set should contain both shopkeeper combat victory locations"
        )

        excluded_locations = friendly_fire_names - existing_location_names
        self.assertTrue(
            killed_mutt_name in excluded_locations and killed_eugene_name in excluded_locations,
            f" {excluded_locations}; Shopkeeper combat victory locations should be excluded when killing shopkeepers is disabled"
        )

        self.assertTrue(len(excluded_locations) == 2,
            f"{len(excluded_locations) - 2} extra locations excluded: {sorted(excluded_locations)}"
            )

class NestorRaftaDisabledItems(LOTestBase):
    options = {
        "goal": PlayerGoal.option_all_endings,
        "include_nestor_quest": False
    }

    def test_nestor_rafta_locations_are_excluded_when_disabled(self):
        nestor_rafta_location_names = location_name_groups["NESTOR_QUEST"]

        existing_location_names = {location.name for location in self.multiworld.get_locations()}

        excluded_locations = nestor_rafta_location_names & existing_location_names

        self.assertTrue(
            len(excluded_locations) == 0,
            f"Nestor worm fight locations should not be created when Nestor quest is disabled: {sorted(excluded_locations)}"
        )
        
    def test_nestor_rafta_items_removed_when_disabled(self):
        nestor_rafta_item_names = item_name_groups["NESTOR_QUEST_INTRO"]

        existing_item_names = {item.name for item in self.multiworld.get_items()}

        excluded_items = nestor_rafta_item_names & existing_item_names

        self.assertTrue(
            len(excluded_items) == 0,
            f"Nestor Rafta items should not be created when Nestor quest is disabled: {sorted(excluded_items)}"
        )

class GameClassificationNoSkillRandomizationTrueFinal(LOTestBase):
    options = {
        "goal": PlayerGoal.option_all_endings,
        "include_game_skills": False
    }

    def test_game_items_are_useful(self):
        game_skill_item_names = item_name_groups["USEFUL_SKILL_VIDEO_GAME"]

        game_items = [item for item in self.multiworld.get_items() if item.name in game_skill_item_names]

        self.assertTrue(
            (game_item.classification == ItemClassification.useful for game_item in game_items), 
            f"Game items should be useful, got: {[(game_item.name, game_item.classification) for game_item in game_items]}")

    def test_massacre_princess_is_progression(self):

        massacre_princess_item_array = [item for item in self.multiworld.get_items() if item.name == "Massacre Princess"]

        self.assertTrue(
            len(massacre_princess_item_array) == 1,
            f"Massacre Princess should be included in the item pool"
        )

        massacre_princess_item = massacre_princess_item_array[0]

        self.assertEqual(
            massacre_princess_item.classification,
            ItemClassification.progression,
            f"Massacre Princess should be progression when game skills are not randomized and true final is part of the goal"
        )

    def skill_items_not_included(self):
        game_skill_item_names = item_name_groups["VIDEO_GAME_SKILL"]

        existing_item_names = {item.name for item in self.multiworld.get_items()}

        excluded_items = game_skill_item_names & existing_item_names

        self.assertTrue(
            len(excluded_items) == 0,
            f"Game skill items should not be created when game skills are not randomized: {sorted(excluded_items)}"
        )

class GameClassificationNoSkillRandomization(LOTestBase):
    options = {
        "goal": PlayerGoal.option_unity,
        "include_game_skills": False
    }

    def test_massacre_princess_is_filler(self):
        massacre_princess_item_array = [item for item in self.multiworld.get_items() if item.name == "Massacre Princess"]

        self.assertTrue(
            len(massacre_princess_item_array) == 1,
            f"Massacre Princess should be included in the item pool"
        )

        massacre_princess_item = massacre_princess_item_array[0]

        self.assertEqual(
            massacre_princess_item.classification,
            ItemClassification.filler,
            f"Massacre Princess should be filler when game skills are not randomized and true final is not part of the goal"
        )

class GameClassificationWithSkillRandomizationTrueFinal(LOTestBase):
    options = {
        "goal": PlayerGoal.option_all_endings,
        "include_game_skills": True
    }

    def test_skill_items_included(self):
        game_skill_item_names = item_name_groups["VIDEO_GAME_SKILL"]

        existing_item_names = {item.name for item in self.multiworld.get_items()}

        excluded_items = game_skill_item_names & existing_item_names

        self.assertTrue(
            len(excluded_items) == len(game_skill_item_names),
            f"Game skill items should all be created when game skills are randomized: {sorted(excluded_items)}"
        )

    def test_game_skills_are_useful(self):
        skill_item_names = item_name_groups["VIDEO_GAME_SKILL"]

        skill_items = [item for item in self.multiworld.get_items() if item.name in skill_item_names and item.name != "Skill: Meteor Strike"]

        self.assertTrue(
            all(skill_item.classification == ItemClassification.useful for skill_item in skill_items), 
            f"All skill items should be useful, got: {[(skill_item.name, skill_item.classification) for skill_item in skill_items]}")

    def test_meteor_strike_is_progression(self):
        meteor_strike_item_array = [item for item in self.multiworld.get_items() if item.name == "Skill: Meteor Strike"]

        self.assertTrue(
            len(meteor_strike_item_array) == 1,
            f"Meteor Strike should be included in the item pool"
        )

        meteor_strike_item = meteor_strike_item_array[0]

        self.assertEqual(
            meteor_strike_item.classification,
            ItemClassification.progression,
            f"Meteor Strike should be progression when game skills are randomized and true final is part of the goal"
        )

    def test_all_games_are_progression(self):
        game_item_names = item_name_groups["VIDEO_GAME"]

        game_items = [item for item in self.multiworld.get_items() if item.name in game_item_names]

        self.assertTrue(
            all(game_item.classification == ItemClassification.progression for game_item in game_items), 
            f"All game items should be progression, got: {[(game_item.name, game_item.classification) for game_item in game_items]}")

class GameClassificationWithSkillRandomizationNoTrueFinal(LOTestBase):
    options = {
        "goal": PlayerGoal.option_promise,
        "include_game_skills": True
    }

    def test_meteor_strike_is_filler(self):
        meteor_strike_item_array = [item for item in self.multiworld.get_items() if item.name == "Skill: Meteor Strike"]

        self.assertTrue(
            len(meteor_strike_item_array) == 1,
            f"Meteor Strike should be included in the item pool"
        )

        meteor_strike_item = meteor_strike_item_array[0]

        self.assertEqual(
            meteor_strike_item.classification,
            ItemClassification.filler,
            f"Meteor Strike should be filler when game skills are randomized and true final is not part of the goal"
        )

class ThreeRandomStartingGamesTest(LOTestBase):
    options = {
        "starting_games": StartingGames.option_random_3
    }

    def test_random_starting_games(self):
        precollected_items = self.multiworld.precollected_items[self.player]

        starting_game_item_names = item_name_groups["VIDEO_GAME"]

        self.assertTrue(
            len(precollected_items) == 3,
            f"Three games should be precollected, got: {precollected_items}"
        )

        self.assertTrue(
            (precollected_item in starting_game_item_names for precollected_item in precollected_items),
            f"Precollected items should be from the video game item group, got: {precollected_items}")

class VanillaRandomStartingGamesTest(LOTestBase):
    options = {
        "starting_games": StartingGames.option_vanilla
    }

    def test_vanilla_starting_games(self):
        precollected_items = self.multiworld.precollected_items[self.player]
        self.assertTrue(
            len(precollected_items) == 3,
            f"Three games should be precollected, got: {len(precollected_items)}"
        )

        precollected_item_names = {item.name for item in precollected_items}

        self.assertTrue(
            ("Myrmidon" in precollected_item_names and "Madwheels 97" in precollected_item_names and "Super Jumplad" in precollected_item_names),
            f"Precollected items should be Myrmidon, Madwheels 97, and Super Jumplad, got: {self.multiworld.precollected_items}")

class MaskLocationsExcluded(LOTestBase):
    options = {
        "include_mask": False
    }

    def test_mask_locations_excluded(self):
        mask_location_names = set(location_table[location_id].str_name for location_id in location_name_groups["MASK_OFFERING"])
        existing_location_names = {location.name for location in self.multiworld.get_locations()}

        excluded_locations = mask_location_names & existing_location_names

        self.assertTrue(
            len(excluded_locations) == 0,
            f"Mask locations should not be created when mask option is disabled: {sorted(excluded_locations)}"
        )

class SybilCombatVictoryWhenPartOfGoal(LOTestBase):
    options = {
        "goal": PlayerGoal.option_all_endings,
        "friendly_fire": False,
    }


    def test_sybil_combat_location_in_all_endings(self):
        existing_location_names = (location.name for location in self.multiworld.get_locations())
        sybil_name = location_table["MEAT_SYBIL_COMBAT_VICTORY"].str_name

        self.assertTrue(
            sybil_name in existing_location_names,
            "Sybil combat victory should be a location when unity is one of the endings"
        )

class SybilCombatVictoryWhenFriendlyFire(LOTestBase):
    options = {
        "goal": PlayerGoal.option_all_roof_endings,
        "friendly_fire": False,
    }

    def test_sybil_excluded_in_friendly_fire(self):
        existing_location_names = (location.name for location in self.multiworld.get_locations())
        sybil_name = location_table["MEAT_SYBIL_COMBAT_VICTORY"].str_name


        self.assertTrue(
            sybil_name not in existing_location_names,
            "Sybil combat victory should not be a location when unity is one of the endings"
        )

# todo: other options