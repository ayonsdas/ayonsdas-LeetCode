class Solution:
    def pathSum(self, nums: List[int]) -> int:
        c = 0
        x = [0 for _ in range(len(nums))]
        x[0] = nums[0] % 10
        for i in range(len(nums)):
            if i == len(nums) - 1:
                c += x[i]
                break
            finder = False
            for j in range(i + 1, len(nums)):
                if nums[j] // 100 == nums[i] // 100 + 1:
                    if (nums[j] // 10) % 10 == (nums[i] // 10) % 10 * 2 or (nums[j] // 10) % 10 == (nums[i] // 10) % 10 * 2 - 1:
                        x[j] = x[i] + nums[j] % 10
                        finder = True
            if not finder:
                c += x[i]
        return c