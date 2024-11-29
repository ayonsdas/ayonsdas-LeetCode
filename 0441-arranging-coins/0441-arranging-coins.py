class Solution:
    def arrangeCoins(self, n: int) -> int:
        return math.floor((-1 + math.sqrt(8 * n + 1)) / 2)