class Solution:
    def concatenatedBinary(self, n: int) -> int:
        t = ""
        for i in range(1, n + 1):
            t += bin(i).split("b")[1]
        return int(t, 2) % (10 ** 9 + 7)