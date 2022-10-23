class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        a = set()
        n = len(words[0])
        for word in words:
            t = sorted([char for char in  word[::2]])
            u = sorted([char for char in word[1::2]])
            i = 0
            j = 0
            x = ""
            for b in range(n):
                if i == j:
                    x += t[i]
                    i += 1
                else:
                    x += u[j]
                    j += 1
            a.add(x)
        return len(list(a))