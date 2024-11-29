class Solution:
    def numDecodings(self, s: str) -> int:
        s = list(map(int, [char for char in s]))
        t = [0] * len(s)
        i = len(s) - 1
        while i >= 0:
            if i == len(s) - 1:
                t[i] = 1 if s[i] != 0 else 0
            elif s[i] != 0:
                t[i] += t[i + 1]
                if s[i] * 10 + s[i + 1] <= 26:
                    t[i] += t[i + 2] if i != len(s) - 2 else 1
            i -= 1
        return t[0]