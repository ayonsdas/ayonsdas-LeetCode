class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function singleNumber($nums) {
        $i = 0;
        for($j = 0; $j < sizeof($nums); $j++)
        {
            $i ^= $nums[$j];
        }
        return $i;
    }
}