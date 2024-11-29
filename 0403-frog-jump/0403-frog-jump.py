class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        s = stones[0]
        
        t = stones[-1]
        
        stones = set(stones)
        
        @lru_cache(None)
        def dp(p: int, pre: int) -> bool:
            
            
            if not p in stones or p > t:
                return False
            
            if p == t:
                return True
            
            return (dp(p + pre - 1, pre - 1) if pre > 1 else False) or dp(p + pre, pre) or dp(p + pre + 1, pre + 1)
            
        
        return dp(s + 1, 1) 