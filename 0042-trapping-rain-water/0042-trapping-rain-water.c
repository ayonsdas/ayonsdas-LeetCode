

int trap(int* height, int heightSize)
{
    int heightL[heightSize];
    int heightR[heightSize];
    for(int i = 0; i < heightSize; i++)
    {
        heightL[i] = 0;
        heightR[i] = 0;
    }

    for(int i = 1; i < heightSize; i++)
    {
        heightL[i] = max(heightL[i - 1], height[i - 1]);
        heightR[heightSize - i - 1] = max(heightR[heightSize - i], height[heightSize - i]);
    }
    int x = 0;
    for(int i = 0; i < heightSize; i++)
    {
        x += max(0, min(heightL[i], heightR[i]) - height[i]);
    }
    return x;
};

int max(int a, int b)
{
    return (a > b) ? a : b;
};

int min(int a, int b)
{
    return (a < b) ? a : b;
};