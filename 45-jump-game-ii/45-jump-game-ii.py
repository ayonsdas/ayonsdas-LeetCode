class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums)] * len(nums)      
        dp[0] = 0
        for i in range(len(nums)):
            di = 0
            while di <= nums[i] and i + di < len(nums):
                dp[i + di] = min([dp[i + di], dp[i] + 1])
                di += 1
        return dp[-1]