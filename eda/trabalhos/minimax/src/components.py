from enum import Enum
from typing import List


class Player(Enum):
    PLAYER_1 = "MAX"
    PLAYER_2 = "MIN"


class Outcome(Enum):
    WIN = 10
    LOSS = -10
    DRAW = 0


class StateNode:
    def __init__(self, position: List[List[str]], value: float, depth: int):
        self.value = value
        self.position = position
        self.depth = depth


class Operator:
    def __init__(self, player: Player, move: str, x: int, y: int):
        self.player = player
        self.move = move
        self.x = x
        self.y = y
