class Solution:
    def maxPower(self, s: str) -> int:
        t = 1
        c = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                c += 1
                t = max(c, t)
            else:
                c = 1
        return t