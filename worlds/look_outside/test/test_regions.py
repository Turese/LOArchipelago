from worlds.look_outside.test.bases import LOTestBase

class RegionAccessTests(LOTestBase):

    # player can access a lot of otherwise blocked by different key areas with the elevator
    def test_elevator_accessability(self):
        state = self.multiworld.state

        self.assertFalse(state.can_reach_region("STAIRWELL", self.player))
        self.assertFalse(state.can_reach_region("FLOOR_1_MAZE", self.player))
        self.assertFalse(state.can_reach_region("FLOOR_2_EAST", self.player))
        self.assertFalse(state.can_reach_region("FLOOR_2_WEST", self.player))
        self.assertFalse(state.can_reach_region("MAILROOM_SHIPPING_WEST_HALL", self.player))
        self.assertFalse(state.can_reach_region("FLOOR_2_WEST", self.player))
        self.assertFalse(state.can_reach_region("BASEMENT_EAST", self.player))
        self.assertFalse(state.can_reach_region("BASEMENT_WEST_PARKING_GARAGE", self.player))
        self.assertFalse(state.can_reach_region("SEWER", self.player))
        self.assertFalse(state.can_reach_region("SEWER_WEST", self.player))
        self.assertFalse(state.can_reach_region("APT_21_LYLE", self.player))

        
        elevator = self.get_item_by_name("Elevator Activation")
        state.collect(elevator)

        self.assertTrue(state.can_reach_region("STAIRWELL", self.player))
        self.assertTrue(state.can_reach_region("FLOOR_1_MAZE", self.player))
        self.assertTrue(state.can_reach_region("FLOOR_2_EAST", self.player))
        self.assertTrue(state.can_reach_region("FLOOR_2_WEST", self.player))
        self.assertTrue(state.can_reach_region("APT_21_LYLE", self.player))
        self.assertTrue(state.can_reach_region("MAILROOM_SHIPPING_WEST_HALL", self.player))
        self.assertTrue(state.can_reach_region("FLOOR_2_WEST", self.player))
        self.assertTrue(state.can_reach_region("BASEMENT_EAST", self.player))
        self.assertTrue(state.can_reach_region("BASEMENT_WEST_PARKING_GARAGE", self.player))
        self.assertTrue(state.can_reach_region("SEWER", self.player))
        self.assertTrue(state.can_reach_region("SEWER_WEST", self.player))

    # player can only reach floor 2 with the padlock key and nothing else
    def test_padlock_key_accessability(self):
        state = self.multiworld.state

        self.assertFalse(state.can_reach_region("STAIRWELL", self.player))
        self.assertFalse(state.can_reach_region("FLOOR_1_MAZE", self.player))
        self.assertFalse(state.can_reach_region("FLOOR_2_EAST", self.player))
        self.assertFalse(state.can_reach_region("FLOOR_2_WEST", self.player))
        self.assertFalse(state.can_reach_region("MAILROOM_SHIPPING_WEST_HALL", self.player))
        self.assertFalse(state.can_reach_region("FLOOR_2_WEST", self.player))
        self.assertFalse(state.can_reach_region("BASEMENT_EAST", self.player))
        self.assertFalse(state.can_reach_region("BASEMENT_WEST_PARKING_GARAGE", self.player))
        self.assertFalse(state.can_reach_region("SEWER", self.player))
        self.assertFalse(state.can_reach_region("SEWER_WEST", self.player))

        key = self.get_item_by_name("Padlock Key")
        state.collect(key)

        self.assertTrue(state.can_reach_region("STAIRWELL", self.player))
        self.assertFalse(state.can_reach_region("FLOOR_1_MAZE", self.player))
        self.assertTrue(state.can_reach_region("FLOOR_2_EAST", self.player))
        self.assertFalse(state.can_reach_region("FLOOR_2_WEST", self.player))
        self.assertFalse(state.can_reach_region("MAILROOM_SHIPPING_WEST_HALL", self.player))
        self.assertFalse(state.can_reach_region("FLOOR_2_WEST", self.player))
        self.assertFalse(state.can_reach_region("BASEMENT_EAST", self.player))
        self.assertFalse(state.can_reach_region("BASEMENT_WEST_PARKING_GARAGE", self.player))
        self.assertFalse(state.can_reach_region("SEWER", self.player))
        self.assertFalse(state.can_reach_region("SEWER_WEST", self.player))
