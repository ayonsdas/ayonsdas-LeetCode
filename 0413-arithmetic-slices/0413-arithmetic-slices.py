class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        currDiff = nums[1] - nums[0]
        c = 0
        m = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == currDiff:
                c += 1
            else:
                c = 0
                currDiff = nums[i] - nums[i - 1]
            m += c
        return m