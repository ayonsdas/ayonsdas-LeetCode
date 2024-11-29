class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) == len(t):
            c = False
            for i in range(len(s)):
                if s[i] != t[i]:
                    if c:
                        return False
                    else:
                        c = True
            return c
        if len(s) < len(t):
            s, t = t, s
        if len(t) == 0:
            return True
        c = False
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if c:
                    return False
                else:
                    c = True
                    i += 1
            else:
                i += 1
                j += 1
        return True