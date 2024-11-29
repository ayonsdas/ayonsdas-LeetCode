class Solution:
    def countHomogenous(self, s: str) -> int:
        t = 1
        c = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                c = 0
            c += 1
            t += c
        return t % (10 ** 9 + 7)