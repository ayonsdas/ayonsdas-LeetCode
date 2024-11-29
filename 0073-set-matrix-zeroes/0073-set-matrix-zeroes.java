class Solution
{
    
    public void setZeroes(int[][] mx)
    {
        int m = mx.length;
        int n = mx[0].length;
        boolean r = false;
        boolean c = false;
        for(int i = 0; i < m; i++)
            if(mx[i][0] == 0)
            {
                c = true;
                break;
            }
        for(int j = 0; j < n; j++)
            if(mx[0][j] == 0)
            {
                r = true;
                break;
            }
        for(int i = 1; i < m; i++)
            for(int j = 1; j < n; j++)
                if(mx[i][j] == 0)
                {
                    mx[0][j] = 0;
                    mx[i][0] = 0;
                }
        for(int i = 1; i < m; i++)
            if(mx[i][0] == 0)
                for(int j = 1; j < n; j++)
                    mx[i][j] = 0;
        for(int j = 1; j < n; j++)
            if(mx[0][j] == 0)
                for(int i = 1; i < m; i++)
                    mx[i][j] = 0;
        if(r)
            for(int j = 0; j < n; j++)
                mx[0][j] = 0;
        if(c)
            for(int i = 0; i < m; i++)
                mx[i][0] = 0;
    }
}