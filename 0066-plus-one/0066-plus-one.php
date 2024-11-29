class Solution {

    /**
     * @param Integer[] $digits
     * @return Integer[]
     */
    function plusOne($digits) {
        $i = sizeof($digits) - 1;
        $do = true;
        while($i > 0)
        {
            $digits[$i] += 1;
            if($digits[$i] != 10)
            {
                $do = false;
                break;
            }
            $digits[$i] = 0;
            $i -= 1;
        }
        if($do)
        {
            if($digits[0] == 9)
            {
                array_unshift($digits, 1);
                $digits[1] = 0;
            }
            else
            {
                $digits[0] += 1;
            }
        }
        return $digits;
    }
}

/**

        i = len(digits) - 1
        while i > 0:
            digits[i] += 1
            if digits[i] != 10:
                break
            digits[i] = 0
            i -= 1
        else:
            if digits[0] == 9:
                digits.insert(0, 1)
                digits[1] = 0
            else:
                digits[0] += 1
        return digits

*/