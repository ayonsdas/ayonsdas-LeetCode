class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        good = set()
        bad = set()
        for i in range(len(fronts)):
            if fronts[i] != backs[i]:
                good.add(fronts[i])
                good.add(backs[i])
            else:
                bad.add(fronts[i])
        x = sorted(list(good))
        i = 0
        while i < len(x):
            if not x[i] in bad:
                return x[i]
            i += 1
        return 0