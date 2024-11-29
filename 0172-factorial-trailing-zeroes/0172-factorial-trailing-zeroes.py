class Solution:
    def trailingZeroes(self, n: int) -> int:
        a = b = n
        i = 0
        j = 0
        while a > 0:
            i += a // 2
            a //= 2
        while b > 0:
            j += b // 5
            b //= 5
        return min(i, j)