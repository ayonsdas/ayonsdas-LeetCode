class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        x1 = -1
        while l <= r:
            m = (l + r) // 2
            if (m == 0 or nums[m - 1] != target) and nums[m] == target:
                x1 = m
                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if x1 == -1:
            return [-1, -1]
        x2 = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if (m == len(nums) - 1 or nums[m + 1] != target) and nums[m] == target:
                x2 = m
                break
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [x1, x2]