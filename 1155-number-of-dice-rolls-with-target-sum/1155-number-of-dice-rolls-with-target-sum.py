class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(target):
                if dp[i][j] != 0:
                    for l in range(1, k + 1):
                        if j + l <= target:
                            dp[i + 1][j + l] += dp[i][j]
        return dp[-1][-1] % (10 ** 9 + 7)