impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut i : usize = 0;
        let mut j : usize = 0;
        while(j < nums.len())
        {
            if(nums[i] != nums[j])
            {
                nums[i + 1] = nums[j];
                i += 1;
            }
            j += 1;
        }
        return (i + 1) as i32;
    }
}