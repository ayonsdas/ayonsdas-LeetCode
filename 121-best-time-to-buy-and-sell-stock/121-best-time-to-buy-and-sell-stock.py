class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        p = 0
        for i in range(1, len(prices)):
            l = min(l, prices[i])
            p = max(p, prices[i] - l)
        return p