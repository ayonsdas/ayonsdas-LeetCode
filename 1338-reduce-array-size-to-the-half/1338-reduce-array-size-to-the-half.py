class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        key = Counter(arr)
        t = sorted(list(key.keys()), key = lambda x : key[x], reverse = True)
        c = 0
        tot = 0
        i = 0
        while tot < math.ceil(len(arr) / 2):
            tot += key[t[i]]
            c += 1
            i += 1
        return c