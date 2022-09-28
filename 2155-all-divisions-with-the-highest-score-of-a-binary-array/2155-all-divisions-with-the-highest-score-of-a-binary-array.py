class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        pSum = [0]
        l = []
        b = 0
        for x in nums:
            pSum.append(pSum[-1] + x)
        for i in range(len(pSum)):
            n = i - pSum[i] + pSum[-1] - pSum[i]
            if n >= b:
                if n > b:
                    l = []
                l.append(i)
                b = n
        return l