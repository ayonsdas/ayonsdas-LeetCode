class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1] if target in set(nums) else [-1, -1]