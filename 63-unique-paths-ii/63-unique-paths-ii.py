class Solution:
    def uniquePathsWithObstacles(self, o: List[List[int]]) -> int:
        dp = [[0 for x in o[0]] for y in o]
        dp[0][0] = 1 - o[0][0]
        for i in range(len(o)):
            for j in range(len(o[0])):
                if o[i][j] != 1 and (i != 0 or j != 0):
                    dp[i][j] = (dp[i - 1][j] if i > 0 else 0) + (dp[i][j - 1] if j > 0 else 0)
        return dp[-1][-1]