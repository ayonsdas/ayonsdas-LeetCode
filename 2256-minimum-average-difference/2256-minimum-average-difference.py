class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        b = float('inf')
        j = 0
        for i in range(len(nums)):
            x = nums[i] // (i + 1)
            y = nums[-1] - nums[i]
            if i != len(nums) - 1:
                y //= (len(nums) - i - 1)
            l = abs(x - y)
            if(l < b):
                b = l
                j = i
        return j