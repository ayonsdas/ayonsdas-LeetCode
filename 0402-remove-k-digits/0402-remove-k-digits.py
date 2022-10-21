class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        for n in num:
            while s and k and s[-1] > n:
                s.pop(-1)
                k -= 1
            if s or n != '0':
                s.append(n)
            
        if k:
            s = s[:-k]
        return ''.join(s) or '0'