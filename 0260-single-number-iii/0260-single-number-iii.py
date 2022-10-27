class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num
        aX = x
        p = 0
        while True:
            if aX % 2 != 0:
                break
            p += 1
            aX //= 2
        
        n1, n2 = 0, 0
        for num in nums:
            if num & 2 ** p == 0:
                n1 ^= num
            else:
                n2 ^= num
        
        return [n1, n2]