impl Solution {
    pub fn reverse_bits(x: u32) -> u32 {
        let mut result : u32 = 0;
        let mut n : u32 = x;
        for i in 0..32
        {
            let j : i32 = 31 - i;
            result |= (n & 1) << j;
            n >>= 1;
        }
        return result;
    }
}