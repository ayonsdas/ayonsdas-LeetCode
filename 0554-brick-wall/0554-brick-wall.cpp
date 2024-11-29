class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        unordered_map<int, int> m;
        int R = wall.size();
        for(int i = 0; i < R; i++)
        {
            int k = 0;
            int C = wall[i].size() - 1;
            for(int j = 0; j < C; j++)
            {
                k += wall[i][j];
                m[k]++;
            }
        }
        
        int macs = 0;
        for (auto &entry: m)
            macs = max(macs, entry.second);
        return wall.size() - macs;
    }
};