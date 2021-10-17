from game import Game
from components import StateNode, Player
from math import inf


class Minimax:

    def minimax(self, state: StateNode, game: Game, turn: Player) -> float:

        if game.is_final(state):
            return game.evaluation_function(state)

        elif turn == Player.PLAYER_1:
            best_value = -inf
            for child in state.children:
                best_value = max(best_value, self.minimax(state=child, game=game, turn=Player.PLAYER_2))
            return best_value

        else:
            best_value = +inf
            for child in state.children:
                best_value = min(best_value, self.minimax(state=child, game=game, turn=Player.PLAYER_1))
            return best_value


if __name__ == '__main__':

    board = [["-" for i in range(3)] for j in range(3)]
    s: StateNode = StateNode(board, -inf)

    tic_tac_toe = Game(s)

    mm = Minimax()
    output = mm.minimax(s, tic_tac_toe, Player.PLAYER_1)
    print(output)

    tic_tac_toe.show_moves()
