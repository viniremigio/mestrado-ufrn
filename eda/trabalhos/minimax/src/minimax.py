from game import Game, TicTacToe
from components import StateNode, Player, Outcome
from math import inf
from timeit import default_timer as timer
from datetime import timedelta


class MiniMax:
    def __init__(self, game: Game, prune: bool, max_depth=None):
        self.game = game
        self.prune = prune
        self.max_depth = max_depth

    def mini_max(self, state: StateNode, depth: int, turn: Player, alpha=None, beta=None) -> (float, StateNode):
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
        if self.prune:
            if depth == self.max_depth:
                return score, state
        else:
            if score == Outcome.WIN.value or score == Outcome.LOSS.value:
                return score, state

        if self.game.is_final(state):
            return 0, state

        elif turn == Player.PLAYER_1:
            best_value = -inf
            pos = state.position
            for x in range(3):
                for y in range(3):
                    if pos[x][y] == "-":
                        op = self.game.operator(turn, x, y)
                        node_depth = depth + 1
                        res, new_state = self.mini_max(state=self.game.apply(state, op, node_depth),
                                                                   depth=node_depth,
                                                                   turn=Player.PLAYER_2,
                                                                   alpha=alpha,
                                                                   beta=beta)
                        best_value = max(best_value, res)
                        pos[x][y] = "-"
                        best_value = best_value - node_depth

                        if self.prune:
                            alpha = max(alpha, best_value)
                            if beta <= alpha:
                                return alpha, new_state

            return best_value, new_state

        else:
            best_value = +inf
            pos = state.position
            for x in range(3):
                for y in range(3):
                    if pos[x][y] == "-":
                        op = self.game.operator(turn, x, y)
                        node_depth = depth + 1
                        res, new_state = self.mini_max(state=self.game.apply(state, op, node_depth),
                                                       depth=node_depth,
                                                       turn=Player.PLAYER_1,
                                                       alpha=alpha,
                                                       beta=beta)
                        best_value = min(best_value, res)
                        pos[x][y] = "-"
                        best_value = best_value + node_depth

                        if self.prune:
                            beta = min(beta, best_value)
                            if beta <= alpha:
                                return beta, new_state

            return best_value, new_state

    def decision(self, state: StateNode, player: Player, alpha=None, beta=None) -> ((int, int), int):
        best_val, best_state = self.mini_max(state, 0, player, alpha, beta)
        return best_val, best_state

    @staticmethod
    def winner(value: float) -> None:
        match_winner = "INDEFINIDO"
        if value > 0:
            match_winner = Player.PLAYER_1.value
        elif value < 0:
            match_winner = Player.PLAYER_2.value
        elif value == 0:
            match_winner = "EMPATE"
        print(f"O vencedor é {match_winner}")
        print(f"Melhor avaliação: {value}")

    def compute_stats(self, state: StateNode) -> None:
        print()
        start = timer()
        (val, state) = self.decision(state, Player.PLAYER_1, -inf, inf)
        self.winner(val)
        print(f"Maior profundidade: {self.game.max_depth}")
        print(f"Poda Alfa-Beta: {self.prune}")
        print(f"Estados gerados: {len(self.game.states)}")

        print()
        self.game.show_board(state)
        print()

        end = timer()
        print(f"Tempo decorrido {str(timedelta(seconds=end-start))}")
        print()


if __name__ == '__main__':

    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['-', '-', '-']
    ]

    # board = [
    #     ['-', '-', '-'],
    #     ['-', '-', '-'],
    #     ['-', '-', '-']
    # ]

    s: StateNode = StateNode(board, -inf, 0)
    tic_tac_toe = TicTacToe(s)

    mm1 = MiniMax(tic_tac_toe, prune=True, max_depth=1)
    mm1.compute_stats(s)
    mm1.game.show_moves()

    s2: StateNode = StateNode(board, -inf, 0)
    tic_tac_toe_2 = TicTacToe(s)

    mm2 = MiniMax(tic_tac_toe_2, prune=False)
    mm2.compute_stats(s2)
    mm2.game.show_moves()
