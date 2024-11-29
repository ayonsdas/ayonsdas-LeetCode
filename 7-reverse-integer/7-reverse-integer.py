class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            return -1 * self.reverse(x * -1)
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x //= 10
        return y if y >= 2 ** 31 * -1 and y < 2 ** 31 else 0