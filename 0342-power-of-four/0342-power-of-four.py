class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return not ((math.log(n) / math.log(4)) % 1) if n > 0 else False