

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize){
    int x = 0;
    for(int i = 0; i < numsSize; i++)
        x ^= nums[i];
    int aX = x, p = 0;
    while(true)
    {
        if(aX % 2 != 0)
            break;
        p += 1;
        aX /= 2;
    }
    int n1 = 0, n2 = 0;
    for(int i = 0; i < numsSize; i++)
    {
        if((nums[i] & (long) 1 << p) == 0)
            n1 ^= nums[i];
        else
            n2 ^= nums[i];
    }
    
    int* a = (int*) malloc(sizeof(int) * 2);
    a[0] = n1;
    a[1] = n2;
    *returnSize = 2;
    return a;
}