class Solution {
    public int maxProfit(int[] prices) {
        int l = prices[0];
        int p = 0;
        for(int i = 1; i < prices.length; i++)
        {
            l = Math.min(l, prices[i]);
            p = Math.max(p, prices[i] - l);
        }
        return p;
    }
}