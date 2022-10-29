class Solution {
    fun removeElement(nums: IntArray, `val`: Int): Int {
        var i : Int = 0;
        for(j in 0..nums.size - 1)
            if(nums[j] != `val`)
                nums[i++] = nums[j];
        return i;
    }
}

/**
        int i = 0;
        for(int j = 0; j < nums.Length; j++)
            if(nums[j] != val)
                nums[i++] = nums[j];
        return i;

*/