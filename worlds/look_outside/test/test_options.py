from worlds.look_outside.test.bases import LOTestBase

class LimitedMovementTest(LOTestBase):
    options = {
        "limited_movement": "true",
        "shuffle_shards": "true",
    }