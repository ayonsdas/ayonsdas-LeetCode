class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        vector<int> rt;
        for(int i = 0; i < grid[0].size(); i++)
        {
            int c = i;
            int r = 0;
            bool x = true;
            while(r <= grid.size() - 1)
            {
                int a = grid[r][c];
                c += grid[r][c];
                if(c < 0 || c >= grid[0].size() || grid[r][c] != a)
                {
                    rt.push_back(-1);
                    x = false;
                    break;
                }
                r += 1;
            }
            if(x)
                rt.push_back(c);
        }
        return rt;
    }
};