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


/*

# @param {Integer[][]} wall
# @return {Integer}
def least_bricks(wall)
    stuff = Hash.new()
    for i in 0..wall.length()-1
        k = 0
        for j in 0..wall[i].length()-2
            k += wall[i][j]
            if not stuff.key?(k)
                stuff[k] = 0
            end
            stuff[k] = stuff[k] + 1
        end
    end
    if stuff.empty?()
        return wall.length()
    end
    return wall.length() - stuff[stuff.max_by{|k, v| v}[0]]
end

*/