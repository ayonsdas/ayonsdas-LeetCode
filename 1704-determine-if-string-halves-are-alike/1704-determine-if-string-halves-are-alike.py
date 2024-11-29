class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = 0
        c = 0
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                if i < len(s) // 2:
                    a += 1
                else:
                    c += 1
        return a == c