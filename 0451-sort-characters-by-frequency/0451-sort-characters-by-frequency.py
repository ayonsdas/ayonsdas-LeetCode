class Solution:
    def frequencySort(self, s: str) -> str:
        s = Counter([char for char in s])
        r = ""
        a = sorted(list(s), key = lambda x : -s[x])
        for l in a:
            for i in range(s[l]):
                r += l
        return r