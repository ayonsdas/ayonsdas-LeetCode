class NumArray {
    /**
     * @param Integer[] $nums
     */
    function __construct($nums) {
        $this->$x = [0];
        for($i = 0; $i < sizeof($nums); $i++)
        {
            array_push($this->$x, $this->$x[sizeof($this->$x) -1] + $nums[$i]);
        }
    }
  
    /**
     * @param Integer $left
     * @param Integer $right
     * @return Integer
     */
    function sumRange($left, $right) {
        return $this->$x[$right + 1] - $this->$x[$left]; 
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * $obj = NumArray($nums);
 * $ret_1 = $obj->sumRange($left, $right);
 */