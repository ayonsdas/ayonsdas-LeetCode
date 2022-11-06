class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 0:
            return s
        if k > 1:
            return "".join(sorted(s))
        st = s
        for i in range(1, len(s)):
            st = min(st, s[i:] + s[0:i])
            
        return st 