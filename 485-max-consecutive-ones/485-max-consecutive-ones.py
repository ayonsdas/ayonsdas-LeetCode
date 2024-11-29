class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        t = 0
        for num in nums:
            if num:
                c += 1
                t = max(t, c)
            else:
                c = 0
        return t