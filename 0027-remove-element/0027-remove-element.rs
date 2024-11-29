impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        if(nums.len() == 0)
        {
            return 0 as i32;
        }
        let mut i : usize = 0;
        for j in 0..nums.len()
        {
            if(nums[j] != val)
            {
                nums[i] = nums[j];
                i = i + 1;
            }
        }
        return i as i32;
    }
}