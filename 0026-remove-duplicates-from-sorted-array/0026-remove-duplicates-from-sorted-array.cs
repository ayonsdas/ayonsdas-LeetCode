public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int i = 0;
        int j = 0;
        while(j < nums.Length) {
            if(nums[i] != nums[j]) {
                nums[++i] = nums[j];
            }
            j++;
        }
        return i + 1;
    }
}