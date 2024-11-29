class Solution {
public:
    int twoSumLessThanK(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int x = -1, i = 0, j = nums.size() - 1;
        while(i < j) {
            if(nums[i] + nums[j] < k)
                x = max(x, nums[i++] + nums[j++]);
            j--;
        }
        return x;
    }
};