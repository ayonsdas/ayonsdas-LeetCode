class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        m = sum(nums)
        c = m
        l = [0]
        for i, num in enumerate(nums, ):
            if num:
                c -= 1
            else:
                c += 1
            if c >= m:
                if c > m:
                    l = []
                l.append(i + 1)
                m = c
        return l