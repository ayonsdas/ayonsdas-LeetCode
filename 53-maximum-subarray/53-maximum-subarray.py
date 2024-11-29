class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        c = nums[0]
        for x in nums[1:]:
            c = x + max(c, 0)
            m = max(m, c)
        return m