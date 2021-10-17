from game import Game, TicTacToe
from components import StateNode, Player
from math import inf


class MiniMax:
    def __init__(self, game: Game):
        self.game = game

    def mini_max(self, state: StateNode, depth: int, turn: Player) -> float:

        if self.game.is_final(state):
            return self.game.evaluation_function(state)

        elif turn == Player.PLAYER_1:
            best_value = -inf
            pos = state.position

            for x in range(3):
                for y in range(3):
                    if pos[x][y] == "-":
                        op = self.game.operator(turn, x, y)
                        node_depth = depth + 1
                        best_value = max(best_value, self.mini_max(state=self.game.apply(op, node_depth),
                                                                  depth=node_depth,
                                                                  turn=Player.PLAYER_2))
            return best_value

        else:
            best_value = +inf
            pos = state.position

            for x in range(3):
                for y in range(3):
                    if pos[x][y] == "-":
                        op = self.game.operator(turn, x, y)
                        node_depth = depth + 1
                        best_value = min(best_value, self.mini_max(state=self.game.apply(op, node_depth),
                                                                  depth=node_depth,
                                                                  turn=Player.PLAYER_1))
            return best_value

    @staticmethod
    def winner(value: float) -> None:
        match_winner = "EMPATE"
        if value == +1:
            match_winner = Player.PLAYER_1
        elif value == -1:
            match_winner = Player.PLAYER_2
        print(f"Valor final: {value}. O vencedor é {match_winner}")


if __name__ == '__main__':

    board = [["-" for i in range(3)] for j in range(3)]
    s: StateNode = StateNode(board, -inf, 0)
    tic_tac_toe = TicTacToe(s)

    mm = MiniMax(tic_tac_toe)
    output = mm.mini_max(s, 0, Player.PLAYER_1)
    mm.winner(output)

    tic_tac_toe.show_moves()
