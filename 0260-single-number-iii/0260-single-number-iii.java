class Solution
{
    public int[] singleNumber(int[] nums)
    {
        int x = 0;
        for(int num : nums)
            x ^= num;
        int aX = x, p = 0;
        while(true)
        {
            if(aX % 2 != 0)
                break;
            p += 1;
            aX /= 2;
        }
        int n1 = 0, n2 = 0;
        for(int num : nums)
            if((num & (int) Math.pow(2, p)) == 0)
                n1 ^= num;
            else
                n2 ^= num;
        return new int[] {n1, n2};
    }
}