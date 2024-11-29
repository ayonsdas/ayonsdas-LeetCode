class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        r = 0
        c = 0
        for i, a in enumerate(values):
            r = max(r, c + a)
            c = max(a, c) - 1
        return r