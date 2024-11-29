class Solution {
public:
    int smallestCommonElement(vector<vector<int>>& mat) {
        unordered_map<int, int> m;
        for(int i = 0; i < mat.size(); i++)
        {
            for(int j = 0; j < mat[i].size(); j++)
            {
                m[mat[i][j]]++;
                if(m[mat[i][j]] == mat.size())
                    return mat[i][j];
            }
        }
        return -1;
    }
};