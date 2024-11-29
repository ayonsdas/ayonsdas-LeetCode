class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        for i in range(1, len(prices)):
            s += max(0, prices[i] - prices[i - 1])
        return s