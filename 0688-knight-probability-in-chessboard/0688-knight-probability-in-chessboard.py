class Solution:
    def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        
        @lru_cache(None)
        def dp(mL, cR, cC):
            if cR < 0 or cR >= n or cC < 0 or cC >= n:
                return 0
            if mL == 0:
                return 1
            m = [(-2, 1), (-1, 2), (2, -1), (1, -2), (1, 2), (2, 1), (-1, -2), (-2, -1)]
            l = 0
            for dx, dy in m:
                l += dp(mL - 1, cR + dx, cC + dy)
            return l / 8
        return dp(k, r, c)