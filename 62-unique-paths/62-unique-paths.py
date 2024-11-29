class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = max(m, n), min(m, n)
        m += n - 2
        n -= 1
        x = 1
        i = 0
        while i < n:
            x *= m
            m -= 1
            i += 1
        for i in range(1, n + 1):
            x //= i
        return x