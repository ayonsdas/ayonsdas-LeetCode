class Solution:
    def maximumEvenSplit(self, f: int) -> List[int]:
        if f % 2 != 0:
            return []
        r = math.floor((1 + math.sqrt(4 * f + 1)) / 2) - 1
        x = [2 * i for i in range(1, r + 1)]
        r = r * (r + 1)
        x[-1] += f - r
        return x