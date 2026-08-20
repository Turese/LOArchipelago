from BaseClasses import CollectionState
from test.general import setup_multiworld

from worlds.look_outside import LookOutsideWorld

from worlds.look_outside.options import PlayerGoal
from worlds.look_outside.test.bases import LOTestBase

# tests if an ending is reachable in collected all states
def ending_test(goal_id):
    multiworld = setup_multiworld(
            LookOutsideWorld,
            options={ "goal": set([goal_id]) }
        )
    assert not multiworld.has_beaten_game(multiworld.state, 1)
    state = CollectionState(multiworld)
    for item in multiworld.get_items():
        state.collect(item, True)
    assert multiworld.completion_condition[1](state)

class TestCompleteableGoals(LOTestBase):
    def test_endings(self):
        ending_test(PlayerGoal.FAILED_RITUAL)
        ending_test(PlayerGoal.ANY_RITUAL)
        ending_test(PlayerGoal.PERFECT_RITUAL)
        ending_test(PlayerGoal.SCREAMING_SKY_ENDING)
        ending_test(PlayerGoal.PROMISE_ENDING)
        ending_test(PlayerGoal.MASK_ENDING)
        ending_test(PlayerGoal.XIN_AMON_ENDING)
        ending_test(PlayerGoal.ETERNAL_FATE_ENDING)
        ending_test(PlayerGoal.UNITY_ENDING)
        ending_test(PlayerGoal.TRUE_FINAL_ENDING)
        ending_test(PlayerGoal.WORDS_OF_POWER_ENDING)
