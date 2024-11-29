class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, 0 - n)
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        else:
            power = self.myPow(x, n // 2)
            if n % 2 == 1:
                return x * power * power
            else:
                return power * power