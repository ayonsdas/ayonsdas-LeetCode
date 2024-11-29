class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        t = m = nums[0]
        for i in range(1, len(nums)):
            m += nums[i]
            t = min(t, m)
        return 1 - min(0, t)