void setZeroes(int** mx, int matrixSize, int* matrixColSize)
{
    bool r = false;
    bool c = false;
    for(int i = 0; i < matrixSize; i++)
    {
        if(mx[i][0] == 0)
        {
            c = true;
            break;
        }
    }
    for(int j = 0; j < *matrixColSize; j++)
    {
        if(mx[0][j] == 0)
        {
            r = true;
            break;
        }
    }
    for(int i = 1; i < matrixSize; i++)
    {
        for(int j = 1; j < *matrixColSize; j++)
        {
            if(mx[i][j] == 0)
            {
                mx[0][j] = 0;
                mx[i][0] = 0;
            }
        }
    }
    for(int i = 1; i < matrixSize; i++)
    {
        if(mx[i][0] == 0)
        {
            for(int j = 1; j < *matrixColSize; j++)
            {
                mx[i][j] = 0;
            }
        }
    }
    for(int j = 1; j < *matrixColSize; j++)
    {
        if(mx[0][j] == 0)
        {
            for(int i = 1; i < matrixSize; i++)
            {
                mx[i][j] = 0;
            }
        }
    }
    if(r)
    {
        for(int j = 0; j < *matrixColSize; j++)
        {
            mx[0][j] = 0;
        }
    }
    if(c)
    {
        for(int i = 0; i < matrixSize; i++)
        {
            mx[i][0] = 0;
        }
    }
}