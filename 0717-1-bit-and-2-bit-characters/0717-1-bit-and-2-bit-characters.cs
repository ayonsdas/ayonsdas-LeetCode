public class Solution {
    public bool IsOneBitCharacter(int[] bits) {
        int r = 0;
        while(r < bits.Length - 1)
        {
            if(bits[r] == 1)
            {
                r += 2;
            }
            else
            {
                r += 1;
            }
        }
        return r == bits.Length - 1;
    }
}