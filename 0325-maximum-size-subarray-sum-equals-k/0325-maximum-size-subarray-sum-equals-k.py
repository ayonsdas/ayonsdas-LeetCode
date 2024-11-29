class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {}
        d[0] = -1
        l = 0
        m = 0
        for i in range(len(nums)):
            l += nums[i]
            if l - k in d and i - d[l - k] > m:
                m = i - d[l - k]
            if not l in d:
                d[l] = i
        return m