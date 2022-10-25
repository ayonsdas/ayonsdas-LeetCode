class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        int curr = Integer.MAX_VALUE;
        int c = 0;
        for(int j = 0; j < nums.length; j++) {
            if(nums[j] != curr) {
                curr = nums[j];
                c = 0;
            }
            c += 1;
            if(c < 3)
                nums[i++] = nums[j];
        }
        return i;
    }
}