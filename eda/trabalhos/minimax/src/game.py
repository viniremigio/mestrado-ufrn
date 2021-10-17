from typing import List
from math import inf
from components import StateNode, Operator, Player
from copy import deepcopy


class Game:
    def __init__(self):
        board = [["X" for i in range(3)] for j in range(3)]
        self.state: StateNode = StateNode(board, -inf)
        self.states: List[StateNode] = [self.state]

    def operators(self):
        op1 = Operator(player=Player.PLAYER_1, move="X", x=0, y=0)
        op2 = Operator(player=Player.PLAYER_2, move="O", x=1, y=0)
        return [op1, op2]

    def is_final(self, state: StateNode) -> bool:
        pos = state.position
        game_over = True
        for i in range(len(pos[0])):
            for j in range(len(pos[1])):
                if pos[i][j] == "-":
                    game_over &= False
        return game_over

    def utility_value(self, state: StateNode) -> float:
        return 0.0

    def apply(self, op: Operator) -> StateNode:
        new_state = deepcopy(self.states[len(self.states)-1])
        new_state.position[op.x][op.y] = op.move
        self.states.append(new_state)
        return new_state

    def show_moves(self):
        for state in self.states:
            self._show_board(state)
            print()

    @staticmethod
    def _show_board(state: StateNode) -> None:
        pos = state.position
        for row in pos:
            for item in row:
                print(item, end=" ")
            print()
