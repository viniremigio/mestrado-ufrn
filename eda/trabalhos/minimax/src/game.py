from typing import List
from components import StateNode, Operator, Player
from copy import deepcopy


class Game:
    def is_final(self, state: StateNode) -> bool:
        pass

    def evaluation_function(self, state: StateNode) -> float:
        pass


class TicTacToe(Game):
    def __init__(self, state: StateNode):
        self.state = state
        self.states: List[StateNode] = [self.state]

    def operators(self):
        op1 = Operator(player=Player.PLAYER_1, move="X", x=0, y=0)
        op2 = Operator(player=Player.PLAYER_2, move="O", x=1, y=0)
        return [op1, op2]

    def is_final(self, state: StateNode) -> bool:
        """
        Determina se o jogo acabou, quando todas as posições foram preenchidas
        :param state: estado a ser avaliado
        :return:
        """
        pos = state.position
        game_over = True
        for i in range(len(pos[0])):
            for j in range(len(pos[1])):
                if pos[i][j] == "-":
                    game_over &= False
        return game_over

    def evaluation_function(self, state: StateNode) -> float:
        board: List[List[str]] = state.position

        # Se houve vencedor nas linhas
        for row in range(0, 3):
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                if board[row][0] == 'X':
                    return +1
                elif board[row][0] == 'O':
                    return -1

        # Se houve vencedor nas colunas
        for col in range(0, 3):
            if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
                if board[0][col] == 'X':
                    return +1
                elif board[0][col] == 'O':
                    return -1

        # Se houve vencedor nas diagonais
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == 'X':
                return +1
            elif board[0][0] == 'O':
                return -1

        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] == 'X':
                return +1
            elif board[0][2] == 'O':
                return -1

        # Houve empate
        else:
            return 0

    def apply(self, op: Operator) -> StateNode:
        new_state = deepcopy(self.states[len(self.states)-1])
        new_state.position[op.x][op.y] = op.move
        self.states.append(new_state)
        return new_state

    def show_moves(self) -> None:
        """
        Imprime o board, mostrando a sequencia de jogadas no tabuleiro
        """
        for state in self.states:
            self._show_board(state)
            print()

    @staticmethod
    def _show_board(state: StateNode) -> None:
        """
        Imprime o estado atual do tabuleiro
        :param state:
        :return:
        """
        pos = state.position
        for row in pos:
            for item in row:
                print(item, end=" ")
            print()
