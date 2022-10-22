class Solution:

    def __init__(self, w: List[int]):
        self.x = w[:]
        for i in range(1, len(self.x)):
            self.x[i] += self.x[i - 1]

    def pickIndex(self) -> int:
        a = random.randint(1, self.x[-1])
        l = 0
        r = len(self.x) - 1
        while l <= r:
            m = (l + r) // 2
            if self.x[m] == a or self.x[m] > a and (m == 0 or self.x[m - 1] < a):
                return m
            elif self.x[m] > a:
                r = m - 1
            else:
                l = m + 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()