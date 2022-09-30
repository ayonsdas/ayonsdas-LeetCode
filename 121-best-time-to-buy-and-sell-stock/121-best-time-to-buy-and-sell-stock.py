class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        p = 0
        for i in range(len(prices)):
            if i == 0:
                l = prices[i]
            else:
                if prices[i] < l:
                    l = prices[i]
                else:
                    p = max(p, prices[i] - l)
        return p