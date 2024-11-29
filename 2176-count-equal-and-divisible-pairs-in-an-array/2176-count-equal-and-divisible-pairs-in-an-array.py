class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    c += 1 if i * j % k == 0 else 0
        return c