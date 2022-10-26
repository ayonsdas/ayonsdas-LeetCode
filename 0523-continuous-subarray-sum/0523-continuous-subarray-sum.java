class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int[] a = new int[nums.length];
        Set<Integer> s = new HashSet<>();
        for(int i = 0; i < nums.length; i++) {
            int r = nums[i] % k;
            if(i == 1) {
                s.add(0);
            }
            else if(i > 1) {
                s.add(a[i - 2]);
            }
            if(i != 0) {
                r = (r + a[i - 1]) % k;
            }
            if(s.contains(r))
                return true;
            a[i] = r;
        }
        return false;
    }
} 