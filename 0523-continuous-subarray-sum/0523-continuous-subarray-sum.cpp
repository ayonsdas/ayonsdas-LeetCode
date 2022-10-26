class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        set<int> s = {};
        for(int i = 0; i < nums.size(); i++) {
            nums[i] %= k;
            if(i != 0) {
                nums[i] = (nums[i] + nums[i - 1]) % k;
            }
            if(i == 1) {
                s.insert(0);
            }
            else if(i > 1) {
                s.insert(nums[i - 2]);
            }
            
            if(bool(s.count(nums[i])))
                return true;
        }
        return false;
    }
};