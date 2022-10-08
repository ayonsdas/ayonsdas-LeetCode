class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums[1:]:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1
        return l