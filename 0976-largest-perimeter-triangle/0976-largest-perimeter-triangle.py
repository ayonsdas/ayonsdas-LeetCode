class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        while nums[2:] and nums[0] >= nums[1] + nums[2]:
            nums = nums[1:]
        if not nums[2:]:
            return 0
        return sum(nums[0:3])