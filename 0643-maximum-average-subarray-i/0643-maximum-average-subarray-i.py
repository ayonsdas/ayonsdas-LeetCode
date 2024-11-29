class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:k])
        m = s
        for i in range(len(nums) - k):
            s += nums[i + k] - nums[i]
            if m < s:
                m = s
        return (m / k)