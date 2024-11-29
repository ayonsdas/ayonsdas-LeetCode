class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        t = [0 for char in s]
        s = [int(char) for char in s]
        for i in range(len(s)):
            if s[~i] != 0:
                j = i - 1
                x = s[~i]
                while j >= 0 and x <= k:
                    t[~i] += t[~j]
                    x *= 10
                    x += s[~j]
                    j -= 1
                if x <= k:
                    t[~i] += 1
                t[~i] %= 10 ** 9 + 7
        return t[0]