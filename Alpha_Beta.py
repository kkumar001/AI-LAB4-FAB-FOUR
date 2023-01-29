class TicTacToe:
    def __init__(self):
        self.board = [[' ' for j in range(3)] for i in range(3)]
        self.player = 'X'
        self.nodes_evaluated = 0

    def alphabeta(self, depth, alpha, beta, maximizingPlayer):
        self.nodes_evaluated += 1
        if depth == 0 or self.game_over():
            return self.evaluate()

        if maximizingPlayer:
            bestValue = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.player
                        value = self.alphabeta(depth - 1, alpha, beta, False)
                        self.board[i][j] = ' '
                        bestValue = max(bestValue, value)
                        alpha = max(alpha, bestValue)
                        if beta <= alpha:
                            break
            return bestValue
        else:
            bestValue = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.get_opponent()
                        value = self.alphabeta(depth - 1, alpha, beta, True)
                        self.board[i][j] = ' '
                        bestValue = min(bestValue, value)
                        beta = min(beta, bestValue)
                        if beta <= alpha:
                            break
            return bestValue

    def get_opponent(self):
        if self.player == 'X':
            return 'O'
        else:
            return 'X'

    def game_over(self):
        # check rows
        for i in range(3):
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return True
        # check columns
        for j in range(3):
            if self.board[0][j] != ' ' and self.board[0][j] == self.board[1][j] and self.board[1][j] == self.board[2][j]:
                return True
        # check diagonals
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return True
        return False

    def evaluate(self):
        if self.game_over():
            if self.player == 'X':
                return 1
            else:
                return -1
        else:
            return 0

game = TicTacToe()
game.alphabeta(9, -float('inf'), float('inf'), True)
print("Nodes evaluated :: ", game.nodes_evaluated)