class Solution {
    fun maxProfit(prices: IntArray): Int {
        var l = prices[0]
        var p = 0
        for(i in 1..prices.size - 1)
        {
            l = if (l < prices[i]) l else prices[i]
            p = if (p > prices[i] - l) p else prices[i] - l
        }
        return p;
    }
}