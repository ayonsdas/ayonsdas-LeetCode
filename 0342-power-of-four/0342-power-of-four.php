class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isPowerOfFour($n) {
        if($n > 0) return (fmod(log($n, 4.0), 1.0) == 0.0); else return false;
    }
}