impl Solution {
    pub fn hammingWeight (n: u32) -> i32 {
        let mut c : i32 = 0;
        let mut x : u32 = n;
        while x > 0
        {
            if (x & 1 != 0)
            {
                c += 1;
            }
            x >>= 1;
        }
        return c;
    }
} 