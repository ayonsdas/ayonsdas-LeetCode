class Solution:
    def minWindow(self, s: str, t: str) -> str:
        a = len(t)
        t = Counter(t)
        r = 0
        l = 0
        b = -1
        while r < len(s):
            while r < len(s) and a > 0:
                if t[s[r]] > 0:
                    a -= 1
                t[s[r]] -= 1
                r += 1
            while l < r and a == 0:
                if s[l] in t:
                    t[s[l]] += 1
                    if t[s[l]] == 1:
                        a += 1
                l += 1
            if l == 0:
                return ""
            if b == -1 or len(b) > r - l + 1:
                b = s[(l - 1):r]
        return b