class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function singleNumber($nums) {
        $x = 0;
        for($i = 0; $i < sizeof($nums); $i++)
            $x ^= $nums[$i];
        $aX = $x;
        $p = 0;
        while(true)
        {
            if($aX % 2 != 0)
                break;
            $p += 1;
            $aX /= 2;
        }
        $n1 = 0;
        $n2 = 0;
        for($i = 0; $i < sizeof($nums); $i++)
        {
            if(($nums[$i] & 2 ** $p) == 0)
                $n1 ^= $nums[$i];
            else
                $n2 ^= $nums[$i];
        }
        return [$n1, $n2];
    }
}
    