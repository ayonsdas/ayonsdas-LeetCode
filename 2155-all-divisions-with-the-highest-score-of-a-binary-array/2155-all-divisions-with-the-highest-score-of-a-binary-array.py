class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        m = c = sum(nums)
        l = [0]
        for i, num in enumerate(nums, start = 1):
            if num:
                c -= 1
            else:
                c += 1
            if c > m:
                l = []
                l.append(i)
                m = c
            elif c == m:
                l.append(i)
        return l