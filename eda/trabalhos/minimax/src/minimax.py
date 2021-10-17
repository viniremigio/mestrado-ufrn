from game import Game
from components import Operator, Player, StateNode


class Minimax:

    def minimax_decision(self, game: Game) -> Operator:
        value_ops = dict()
        for operator in game.operators():
            value = self.minimax_value(game.apply(operator), game, Player.PLAYER_1)
            value_ops.update({operator: value})
        return max(value_ops)

    def minimax_value(self, state: StateNode, game: Game, player_turn: Player) -> float:
        if game.is_final(state):
            return game.utility_value(state)
        elif player_turn == Player.PLAYER_1:
            return max(self.minimax_value(state, game, Player.PLAYER_2))
        else:
            return min(self.minimax_value(state, game, Player.PLAYER_1))


if __name__ == '__main__':
    tic_tac_toe = Game()
    ops = tic_tac_toe.operators()

    mm = Minimax()
    mm.minimax_decision(tic_tac_toe)
    tic_tac_toe.show_moves()


# TODO
"""
Como gerar novas jogadas
Como representar as possibilidades
Como calcular a utilidade
"""
