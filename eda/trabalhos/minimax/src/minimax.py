from game import Game, TicTacToe
from components import StateNode, Player
from math import inf


class MiniMax:
    def __init__(self, game: Game):
        self.game = game

    def mini_max(self, state: StateNode, depth: int, turn: Player) -> float:

        score = self.game.evaluation_function(state)
        if score == +1 or score == -1:
            return score

        if self.game.is_final(state):
            return 0

        elif turn == Player.PLAYER_1:
            best_value = -inf
            pos = state.position

            for x in range(3):
                for y in range(3):
                    if pos[x][y] == "-":
                        op = self.game.operator(turn, x, y)
                        node_depth = depth + 1
                        best_value = max(best_value, self.mini_max(state=self.game.apply(state, op, node_depth),
                                                                   depth=node_depth,
                                                                   turn=Player.PLAYER_2))
                        pos[x][y] = "-"
            return best_value

        else:
            best_value = +inf
            pos = state.position

            for x in range(3):
                for y in range(3):
                    if pos[x][y] == "-":
                        op = self.game.operator(turn, x, y)
                        node_depth = depth + 1
                        best_value = min(best_value, self.mini_max(state=self.game.apply(state, op, node_depth),
                                                                   depth=node_depth,
                                                                   turn=Player.PLAYER_1))
                        pos[x][y] = "-"
            return best_value

    def best_move(self, state: StateNode, player: Player) -> ((int, int), int):
        best_val = -inf
        best_move = (-1, -1)

        board = state.position
        for i in range(3):
            for j in range(3):

                if board[i][j] == "-":
                    op = self.game.operator(player, i, j)
                    new_state = self.game.apply(state, op, 1)

                    opponent = Player.PLAYER_2 if player == Player.PLAYER_1 else Player.PLAYER_2
                    val = self.mini_max(new_state, 1, opponent)
                    board[i][j] = "-"

                    if val > best_val:
                        best_move = (i, j)
                        best_val = val
        return best_move, best_val

    @staticmethod
    def winner(value: float) -> None:
        match_winner = "EMPATE"
        if value == +1:
            match_winner = Player.PLAYER_1.value
        elif value == -1:
            match_winner = Player.PLAYER_2.value
        print(f"Valor final: {value}. O vencedor é {match_winner}")


if __name__ == '__main__':

    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['-', '-', '-']
    ]

    s: StateNode = StateNode(board, -inf, 0)
    tic_tac_toe = TicTacToe(s)

    mm = MiniMax(tic_tac_toe)
    move, val = mm.best_move(s, Player.PLAYER_1)

    mm.winner(val)
    print(f"Best move: {move}")

    tic_tac_toe.show_moves()
