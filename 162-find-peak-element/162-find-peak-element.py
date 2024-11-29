class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums[1:]:
            return 0
        for i in range(len(nums)):
            if i == 0:
                if nums[1] < nums[0]:
                    return i
            elif i == len(nums) - 1:
                if nums[-2] < nums[-1]:
                    return i
            else:
                if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                    return i