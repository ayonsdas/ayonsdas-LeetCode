class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if math.sqrt(c) % 1 == 0:
            return True
        l = 0
        r = int(math.sqrt(c))
        while r > l:
            m = r ** 2 + l ** 2
            if m > c:
                r -= 1
            elif m < c:
                l += 1
            else:
                return True
        return l ** 2 + r ** 2 == c