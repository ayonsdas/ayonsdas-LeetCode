class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k = set()
        for num in nums:
            if num > 0 and num <= len(nums):
                k.add(num)
        for i in range(1, len(nums)):
            if not i in k:
                return i
        return len(k) + 1