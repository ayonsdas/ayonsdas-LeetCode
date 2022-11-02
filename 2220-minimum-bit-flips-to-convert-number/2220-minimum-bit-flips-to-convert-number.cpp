class Solution {
public:
    int minBitFlips(int start, int goal) {
        int f = start ^ goal;
        int c = 0;
        while(f > 0)
        {
            if(f % 2 == 1)
                c++;
            f >>= 1;
        }    
        return c;
    }
}; 