class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[row] += 1 if player == 1 else -1
        if self.rows[row] == self.n:
            return 1
        elif self.rows[row] == -self.n:
            return 2
        self.cols[col] += 1 if player == 1 else -1
        if self.cols[col] == self.n:
            return 1
        elif self.cols[col] == -self.n:
            return 2
        if row == col:
            self.diag1 += 1 if player == 1 else -1
            if self.diag1 == self.n:
                return 1
            elif self.diag1 == -self.n:
                return 2
        if row + col == self.n - 1:
            self.diag2 += 1 if player == 1 else -1
            if self.diag2 == self.n:
                return 1
            elif self.diag2 == -self.n:
                return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)