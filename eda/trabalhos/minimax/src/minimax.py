from typing import List, Any
from copy import deepcopy, copy


class Operator:
    def __init__(self, player: str, move: str, x: int, y: int):
        self.player = player
        self.move = move
        self.x = x
        self.y = y


class Game:
    def __init__(self):
        self.state: List[List[str]] = [["-" for i in range(3)] for j in range(3)]
        self.states = [self.state]

    def operators(self):
        op1 = Operator(player="MAX", move="X", x=0, y=0)
        op2 = Operator(player="MIN", move="O", x=1, y=0)
        return [op1, op2]

    def is_final(self, state: List[List[str]]) -> bool:
        game_over = True
        for i in range(len(state[0])):
            for j in range(len(state[1])):
                if state[i][j] == "-":
                    game_over &= False
        return game_over

    def utility_value(self, state: List[List[str]]) -> float:
        return 0.0

    def apply(self, op: Operator) -> List[List[str]]:
        new_state = deepcopy(self.states[len(self.states)-1])
        new_state[op.x][op.y] = op.move
        self.states.append(new_state)
        return new_state

    def show_moves(self):
        for state in self.states:
            self.show_board(state)
            print()

    def show_board(self, state):
        for row in state:
            for item in row:
                print(item, end=" ")
            print()
        return self


class Minimax:
    def __init__(self):
        self.turn = "MAX"

    def minimax_decision(self, game: Game) -> Operator:
        value_ops = dict()
        for operator in game.operators():
            value = self.minimax_value(game.apply(operator), game)
            value_ops.update({operator: value})
        return max(value_ops)

    def minimax_value(self, state: List[List[str]], game: Game) -> float:
        if game.is_final(state):
            return game.utility_value(state)
        elif self.turn == "MAX":
            return max(self.minimax_value(state, game))
        else:
            return min(self.minimax_value(state, game))


if __name__ == '__main__':
    game = Game()
    ops = game.operators()

    mm = Minimax()
    mm.minimax_decision(game)
    game.show_moves()


# TODO
"""
Como gerar novas jogadas
Como representar as possibilidades
Como calcular a utilidade
"""
