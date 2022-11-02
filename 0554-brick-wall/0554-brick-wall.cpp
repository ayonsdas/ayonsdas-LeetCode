class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        map<int, int> m;
        for(int i = 0; i < wall.size(); i++)
        {
            int k = 0;
            for(int j = 0; j < wall[i].size() - 1; j++)
            {
                k += wall[i][j];
                m[k] += 1;
            }
        }
        
        int macs = 0;
        for (const auto &entry: m)
        {
            if (macs < entry.second)
            {
                macs = entry.second;
            }
        }
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