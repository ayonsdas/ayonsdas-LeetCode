class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.x = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.x[i][j] = matrix[i][j] + (self.x[i - 1][j] if i > 0 else 0) + (self.x[i][j - 1] if j > 0 else 0) - (self.x[i - 1][j - 1] if (i > 0 and j > 0) else 0)
        print(self.x)

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.x[r2][c2] - (self.x[r1 - 1][c2] if r1 > 0 else 0) - (self.x[r2][c1 - 1] if c1 > 0 else 0) + (self.x[r1 - 1][c1 - 1] if (r1 > 0 and c1 > 0) else 0)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)