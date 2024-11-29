class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(x, y):
            if y == len(p):
                return x == len(s)

            if x < len(s) and (s[x] == p[y] or p[y] == '?'):
                return dfs(x + 1, y + 1)
            
            if p[y] == '*':
                return dfs(x, y + 1) or x < len(s) and dfs(x + 1, y)
            
            return False

        return dfs(0, 0)