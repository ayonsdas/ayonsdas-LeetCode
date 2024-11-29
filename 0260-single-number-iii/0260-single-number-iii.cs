public class Solution {
    public int[] SingleNumber(int[] nums) {
        int x = 0;
        for(int i = 0; i < nums.Length; i++)
            x ^= nums[i];
        int aX = x, p = 0;
        while(true)
        {
            if(aX % 2 != 0)
                break;
            p += 1;
            aX /= 2;
        }
        int n1 = 0, n2 = 0;
        for(int i = 0; i < nums.Length; i++)
            if((nums[i] & (int) Math.Pow(2, p)) == 0)
                n1 ^= nums[i];
            else
                n2 ^= nums[i];
        return new int[] {n1, n2};
    }
}