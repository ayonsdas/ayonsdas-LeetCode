public class Solution {
    public int NumSubarrayProductLessThanK(int[] nums, int k) {
        int product = 1;
        int count = 0;
        int left = 0;
        for(int right = 0; right < nums.Length; right++) {
            product *= nums[right];
            while(left <= right && product >= k) {
                product /= nums[left];
                left += 1;
            }
            count += right - left + 1;
        }
        return count;
    }
}