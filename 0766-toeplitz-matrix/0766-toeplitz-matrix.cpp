class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size() - 1;
        int n = 0;
        for(int i = 0; i < matrix.size() + matrix[0].size() - 1; i++)
        {
            int x = m, y = n;
            while(x < matrix.size() && y < matrix[0].size())
                if(matrix[x++][y++] != matrix[m][n])
                    return false;
            
            if(m > 0)
                m--;
            else
                n++;
        }
        return true;
    }
};