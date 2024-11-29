public class Solution {
    public int Search(int[] nums, int target) {
        int l = 0, r = nums.Length;
        
        while(l < r)
        {
            int m = (l + r) / 2;
            if(nums[m] == target)
            {
                return m;
            }
            else if(nums[m] > target)
            {
                r = m - 1;
            }
            else
            {
                l = m + 1;
            }
            
        }
        if(r >= 0 && r < nums.Length && nums[r] == target)
        {
            return r;
        }
        return -1;
    }
}