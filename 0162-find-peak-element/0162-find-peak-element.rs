impl Solution {
    pub fn find_peak_element(nums: Vec<i32>) -> i32 {
        
        fn search(nums: &[i32], l: usize, r: usize) -> usize
        {
            if l == r
            {
                return l;
            }
            let m : usize = l + (r - l) / 2;
            if nums[m] > nums[m + 1]
            {
                return search(nums, l, m);
            }
            return search(nums, m + 1, r);
        }
        
        return search(&nums, 0, nums.len() - 1) as i32;
    }
}