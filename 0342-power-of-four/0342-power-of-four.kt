class Solution {
    fun isPowerOfFour(n: Int): Boolean {
        return if (n > 0) ((Math.log(n.toDouble()) / Math.log(4.0)) % 1.0 == 0.0) else false;
    }
}


/*
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return not ((math.log(n) / math.log(4)) % 1) if n > 0 else False
        
*/