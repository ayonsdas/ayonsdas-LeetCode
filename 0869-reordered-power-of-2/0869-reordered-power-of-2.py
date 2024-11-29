from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        b = []
        for i in range(31):
            b.append(Counter(list(str(1<<i))))
        t = Counter(list(str(n)))
        return t in b