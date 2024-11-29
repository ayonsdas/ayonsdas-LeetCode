class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        x = -1
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] < k:
                x = max(x, nums[i] + nums[j])
                i += 1
            else:
                j -= 1
            
        return x