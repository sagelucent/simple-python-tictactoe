class TicTacToeGame:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None
        self.is_tie = False
        self.move_count = 0

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.winner and not self.is_tie:
            self.board[row][col] = self.current_player
            self.move_count += 1
            
            if self.check_winner():
                self.winner = self.current_player
            elif self.check_tie():
                self.is_tie = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_tie(self):
        return self.move_count == 9 and not self.winner

    def reset(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None
        self.is_tie = False
        self.move_count = 0

