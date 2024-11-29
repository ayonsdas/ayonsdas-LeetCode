class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int c = 1;
        int curr = 10001;
        int i = 0;
        for(int j = 0; j < nums.size(); j++) {
            if(nums[j] != curr) {
                curr = nums[j];
                c = 0;
            }
            c += 1;
            if (c < 3) {
                nums[i++] = nums[j];
            }
            
        }
        return i;
    }
};