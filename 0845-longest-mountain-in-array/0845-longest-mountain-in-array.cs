public class Solution {
    public int LongestMountain(int[] arr) {
        int[] dp = new int[arr.Length];
        int[] dp2 = new int[arr.Length];
        int c1 = 0;
        int c2 = 0;
        for(int i = 1; i < arr.Length - 1; i++)
        {
            int j = arr.Length - i - 1;
            if(arr[i] > arr[i - 1])
            {
                c1 += 1;
            }
            else
            {
                c1 = 0;
            }
            if(arr[j] > arr[j + 1])
            {
                c2 += 1;
            }
            else
            {
                c2 = 0;
            }
            dp[i] = c1;
            dp2[j] = c2;
        }
        for(int i = 1; i < arr.Length - 1; i++)
        {
            if(dp[i] == 0 || dp2[i] == 0)
            {
                dp[i] = 0;
            }
            else
            {
                dp[i] += dp2[i] + 1;
            }
        }
        return dp.Max();
    }
}