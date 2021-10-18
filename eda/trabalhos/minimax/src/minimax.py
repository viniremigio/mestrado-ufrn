from game import Game, TicTacToe
from components import StateNode, Player
from typing import List
from math import inf
from timeit import default_timer as timer
from datetime import timedelta


class MiniMax:
    def __init__(self, game: Game, prune: bool):
        self.game = game
        self.prune = prune

    def mini_max(self, state: StateNode, depth: int, turn: Player, alpha=None, beta=None) -> float:
        """
        Algoritmo Minimax
        :param beta:
        :param alpha:
        :param state: Estado do tabuleiro
        :param depth: profundidade da árvore
        :param turn: jogador que possui a vez de jogar
        :return: Se MAX vencer retorna 1;
                 Se MIN vencer retorna -1;
                 Se o tabuleiro for preenchido e ninguém vencer, dá empate, retorna 0.
        """
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
                                                                   turn=Player.PLAYER_2,
                                                                   alpha=alpha,
                                                                   beta=beta))
                        pos[x][y] = "-"
                        best_value -= node_depth

                        if self.prune:
                            alpha = max(alpha, best_value)
                            if beta <= alpha:
                                break

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
                                                                   turn=Player.PLAYER_1,
                                                                   alpha=alpha,
                                                                   beta=beta))
                        pos[x][y] = "-"
                        best_value += node_depth

                        if self.prune:
                            beta = min(beta, best_value)
                            if beta <= alpha:
                                break
            return best_value

    def best_move(self, state: StateNode, player: Player, alpha=None, beta=None) -> ((int, int), int):
        best_val = -inf
        best_move = (-1, -1)

        board = state.position
        for i in range(3):
            for j in range(3):

                if board[i][j] == "-":
                    op = self.game.operator(player, i, j)
                    new_state = self.game.apply(state, op, 1)

                    opponent = Player.PLAYER_2 if player == Player.PLAYER_1 else Player.PLAYER_1
                    val = self.mini_max(new_state, 1, opponent, alpha, beta)
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

    def compute_stats(self, state: StateNode) -> None:
        start = timer()
        move, val = self.best_move(state, Player.PLAYER_1, -inf, inf)
        self.winner(val)
        print(f"Maior profundidade: {self.game.max_depth}")
        print(f"Melhor movimento: {move}")
        end = timer()
        print(timedelta(seconds=end-start))


if __name__ == '__main__':

    # board = [
    #     ['X', 'O', 'X'],
    #     ['O', 'O', 'X'],
    #     ['-', '-', '-']
    # ]

    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

    s: StateNode = StateNode(board, -inf, 0)
    tic_tac_toe = TicTacToe(s)

    mm1 = MiniMax(tic_tac_toe, prune=True)
    mm1.compute_stats(s)

    mm2 = MiniMax(tic_tac_toe, prune=False)
    mm2.compute_stats(s)



