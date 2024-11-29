class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = []
        for n in nums:
            if nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] *= -1
            else:
                a.append(abs(n))
        return a