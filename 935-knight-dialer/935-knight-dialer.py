class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [[1 for _ in range(3)] for _ in range(3)]
        dp.append([0, 1, 0])
        valid = [[[[1, 2], [2, 1]], [[2, 0], [2, 2]], [[1, 0], [2, 1]]],
                 [[[0, 2], [2, 2], [3, 1]], [], [[0, 0], [2, 0], [3, 1]]],
                 [[[0, 1], [1, 2]], [[0, 0], [0, 2]], [[0, 1], [1, 0]]],
                 [[], [[1, 0], [1, 2]], []]]
        for i in range(1, n):
            dp2 = []
            for t in dp:
                x = []
                for l in t:
                    x.append(0)
                dp2.append(x)
            for j in range(len(dp)):
                for k in range(len(dp[0])):
                    for t in valid[j][k]:
                        dp2[j][k] += dp[t[0]][t[1]]
            dp = dp2 
        return sum([sum(r) for r in dp]) % (10 ** 9 + 7)