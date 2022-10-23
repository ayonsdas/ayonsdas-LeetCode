class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        a = 0
        for i in range(30):
            c = 0
            d = 0
            for i in range(len(nums)):
                if nums[i] & 1:
                    c += 1
                else:
                    d += 1
                nums[i] >>= 1
            a += c * d
        return a