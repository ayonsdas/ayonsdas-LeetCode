class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = [[0 for _ in grid[0]] for _ in grid]
        dp[-1][-1] = grid[-1][-1]
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    continue
                if i == len(grid) - 1:
                    dp[i][j] = dp[i][j + 1] + grid[i][j]
                elif j == len(grid[0]) - 1:
                    dp[i][j] = dp[i + 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]
        return dp[0][0]