class Solution:
    def longestPrefix(self, s: str) -> str:
        l = 0
        r = 0
        b = 0
        for i in range(len(s) - 1):
            l = (l * 128 + ord(s[i])) % (10 ** 9 + 7)
            r = (r + pow(128, i, 10 ** 9 + 7) * (ord(s[~i]))) % (10 ** 9 + 7)
            if l == r:
                b = i + 1
        return s[:b]