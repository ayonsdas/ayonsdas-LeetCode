class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        x = []
        for word in arr:
            l = set()
            for char in word:
                if char in l:
                    break
                l.add(char)
            else:
                x.append(word)
        def dp(s: str, p: int) -> str:
            nonlocal x
            if p == len(x):
                return s
            a = set(s)
            b = set(x[p])
            c = dp(s, p + 1)
            if len(list(a & b)) == 0:
                d = dp(s + x[p], p + 1)
                if len(d) > len(c):
                    c = d
            return c
            
        return len(dp("", 0))