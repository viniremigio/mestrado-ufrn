from game import Game
from components import Player, StateNode
from math import inf


class Minimax:

    def minimax_decision(self, state: StateNode, game: Game) -> float:
        value = self.minimax_value(state, game, Player.PLAYER_1)
        return value

    def minimax_value(self, state: StateNode, game: Game, player_turn: Player) -> float:
        if game.is_final(state):
            return game.utility_value(state)

        elif player_turn == Player.PLAYER_1:
            value = -inf
            for child in state.children:
                value = max(value, self.minimax_value(child, game, Player.PLAYER_2))
            return value

        else:
            value = +inf
            for child in state.children:
                value = min(value, self.minimax_value(child, game, Player.PLAYER_1))
            return value


if __name__ == '__main__':

    board = [["-" for i in range(3)] for j in range(3)]
    s: StateNode = StateNode(board, -inf)

    tic_tac_toe = Game(s)

    mm = Minimax()
    output = mm.minimax_decision(s, tic_tac_toe)
    print(output)

    tic_tac_toe.show_moves()


# TODO
"""
Como gerar novas jogadas
Como representar as possibilidades
Como calcular a utilidade
"""
