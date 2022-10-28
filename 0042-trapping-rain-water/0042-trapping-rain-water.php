class Solution {

    /**
     * @param Integer[] $height
     * @return Integer
     */
    function trap($height)
    {
        $heightL = [];
        $heightR = [];
        array_push($heightL, 0);
        array_push($heightR, 0);
        for($i = 1; $i < sizeof($height); $i++)
        {
            array_push($heightL, max($heightL[sizeof($heightL) - 1], $height[$i - 1]));
            array_push($heightR, max($heightR[sizeof($heightR) - 1], $height[sizeof($height) - $i]));
        }
        $x = 0;
        for($i = 0; $i < sizeof($height); $i++)
        {
            $x += max(0, min($heightL[$i], $heightR[sizeof($height) - $i - 1]) - $height[$i]);
        }
        return $x;
    }
}

/**
# @param {Integer[]} height
# @return {Integer}
def trap(height)
    heightL = [0]
    heightR = [0]
    for i in 1..height.length() - 1
        heightL.push([heightL[-1], height[i - 1]].max())
        heightR.unshift([heightR[0], height[-i]].max())
    end
    x = 0
    for i in 0..height.length() - 1
        x += [0, [heightL[i], heightR[i]].min() - height[i]].max()
    end
    return x
end
*/