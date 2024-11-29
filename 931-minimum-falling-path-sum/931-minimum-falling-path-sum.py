class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        t = [[float('inf') for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix[0])):
            t[-1][i] = matrix[-1][i]
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                x = float('inf')
                if j > 0:
                    x = min(x, t[-i][j - 1])
                if j < len(matrix[0]) - 1:
                    x = min(x, t[-i][j + 1])
                x = min(x, t[-i][j])
                t[~i][j] = matrix[~i][j] + x
        return min(t[0])