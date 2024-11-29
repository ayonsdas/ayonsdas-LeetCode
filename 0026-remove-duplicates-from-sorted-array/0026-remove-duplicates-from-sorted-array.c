

int removeDuplicates(int* nums, int numsSize){
    int i = 0;
    int j = 0;
    while(j < numsSize) {
        if(nums[i] != nums[j]) {
            nums[++i] = nums[j];
        }
        j++;
    }
    return i + 1;
}