class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0
        cr = 2 ** 31 - 1
        i = 0
        for j in range(len(nums)):
            if nums[j] != cr:
                cr = nums[j]
                c = 0
            c += 1
            if c < 3:
                nums[i] = nums[j]
                i += 1
        return i 