class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if maxReach < i:
                return False
            if maxReach >= len(nums) - 1:
                return True
            maxReach = max([i + nums[i], maxReach])
        return maxReach >= len(nums) - 1