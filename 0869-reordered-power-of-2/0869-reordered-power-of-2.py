from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        a = 1
        b = set()
        for i in range(30):
            b.add(a)
            a *= 2
        t = set(["".join(a) if a[0] != '0' else '9999' for a in permutations([char for char in str(n)])])
        for x in b:
            if str(x) in t:
                return True
        return False