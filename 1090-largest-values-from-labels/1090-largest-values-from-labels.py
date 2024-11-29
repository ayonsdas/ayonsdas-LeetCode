class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        key = []
        for i in range(len(values)):
            key.append([values[i], labels[i]])
        key = sorted(key, key = lambda x : -x[0])
        used = defaultdict(int)
        a = 0
        s = 0
        i = 0
        while a < numWanted and i < len(key):
            if used[key[i][1]] < useLimit:
                used[key[i][1]] += 1
                a += 1
                s += key[i][0]
            i += 1
        return s