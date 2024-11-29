public class Solution {
    public int SingleNumber(int[] nums) {
        int i = 0;
        for(int j = 0; j < nums.Length; j++)
        {
            i ^= nums[j];
        }
        return i;
    }
}