class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        c = 0
        f = {}
        for i in range(len(keyboard)):
            f[keyboard[i]] = i
        m = 0
        for i in range(len(word)):
            c += abs(f[word[i]] - m)
            m = f[word[i]]
        return c