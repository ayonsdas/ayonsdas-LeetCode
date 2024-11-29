class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache
        def dp (x: int, y: int) -> int:
            nonlocal word1, word2
            
            if x == len(word1):
                return len(word2) - y
            
            if y == len(word2):
                return len(word1) - x
            
            if word1[x] == word2[y]:
                return dp(x + 1, y + 1)
            
            return 1 + min(dp(x + 1, y), dp(x, y + 1), dp(x + 1, y + 1))
        
        return dp(0, 0)