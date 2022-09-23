class Solution:
    def concatenatedBinary(self, n: int) -> int:
        t = 1
        for i in range(2, n + 1):
            t *= 2 ** int(math.log2(i) + 1)
            t += i
            t %= 10 ** 9 + 7
        return t