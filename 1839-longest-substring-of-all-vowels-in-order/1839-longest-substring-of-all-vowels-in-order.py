class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        c = 0
        p = -1
        m = 0
        v = ['a', 'e', 'i', 'o', 'u']
        for char in word:
            a = v.index(char)
            if a == p + 1:
                p += 1
                c += 1
                if a == 4:
                    m = max(m, c)
            elif a == p:
                c += 1
                if a == 4:
                    m = max(m, c)
            else:
                c = 0
                p = -1
                if a == 0:
                    p = 0
                    c = 1
        return m