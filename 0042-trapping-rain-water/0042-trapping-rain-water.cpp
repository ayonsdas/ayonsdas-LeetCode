class Solution {
public:
    int trap(vector<int>& height) {
        int heightL[height.size()];
        int heightR[height.size()];
        for(int i = 0; i < height.size(); i++)
        {
            heightL[i] = 0;
            heightR[i] = 0;
        }
        
        for(int i = 1; i < height.size(); i++)
        {
            heightL[i] = std::max(heightL[i - 1], height[i - 1]);
            heightR[height.size() - i - 1] = std::max(heightR[height.size() - i], height[height.size() - i]);
        }
        int x = 0;
        for(int i = 0; i < height.size(); i++)
        {
            x += std::max(0, std::min(heightL[i], heightR[i]) - height[i]);
        }
        return x;
    }
};