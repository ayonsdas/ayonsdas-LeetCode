class Solution:
    def numSub(self, s: str) -> int:
        c = 0
        m = 0
        for a in s:
            if a == '1':
                c += 1
            else:
                c = 0
            m += c
        return m % (10 ** 9 + 7)