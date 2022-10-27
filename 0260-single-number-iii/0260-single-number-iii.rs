impl Solution {
    pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
        let mut x : i32 = 0;
        for i in 0..nums.len()
        {
            x ^= nums[i];
        }
        let mut aX : i32 = x;
        let mut p : i32 = 1;
        loop
        {
            if aX % 2 != 0
            {
                break;
            }
            p <<= 1;
            aX /= 2;
        }
        let mut n1 : i32 = 0;
        let mut n2 : i32 = 0;
        for i in 0..nums.len()
        {
            if(nums[i] & p == 0)
            {
                n1 ^= nums[i];
            }
            else
            {
                n2 ^= nums[i];
            }
        }
        return [n1, n2].to_vec();
    }
}