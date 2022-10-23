class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        a = 0
        b = 1
        for i in range(30):
            c = 0
            d = 0
            for i in range(len(nums)):
                if nums[i] & b:
                    c += 1
                else:
                    d += 1
            a += c * d
            b *= 2
        return a