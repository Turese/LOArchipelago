from BaseClasses import CollectionState
from test.general import setup_multiworld

from worlds.look_outside import LookOutsideWorld

from worlds.look_outside.options import PlayerGoal
from worlds.look_outside.test.bases import LOTestBase

# tests if an ending is reachable in collected all states
def ending_test(goal_id):
    multiworld = setup_multiworld(
            LookOutsideWorld,
            options={ "goal": goal_id }
        )
    assert not multiworld.has_beaten_game(multiworld.state, 1)
    state = CollectionState(multiworld)
    for item in multiworld.get_items():
        state.collect(item, True)
    assert multiworld.completion_condition[1](state)

class TestCompleteableGoals(LOTestBase):
    def test_endings(self):
        ending_test(PlayerGoal.option_any_partial_ritual_ending)
        ending_test(PlayerGoal.option_any_perfect_ritual_ending)
        ending_test(PlayerGoal.option_screaming_sky)
        ending_test(PlayerGoal.option_promise)
        ending_test(PlayerGoal.option_mask)
        ending_test(PlayerGoal.option_xin_amon)
        ending_test(PlayerGoal.option_unity)
        ending_test(PlayerGoal.option_true_final)
        ending_test(PlayerGoal.option_all_roof_endings)
        ending_test(PlayerGoal.option_all_endings)