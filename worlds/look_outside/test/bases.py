from typing import ClassVar

from test.bases import WorldTestBase
from worlds.look_outside import LookOutsideWorld


class LOTestBase(WorldTestBase):
    game = "Look Outside"

    player: ClassVar[int] = 1

    world: LookOutsideWorld