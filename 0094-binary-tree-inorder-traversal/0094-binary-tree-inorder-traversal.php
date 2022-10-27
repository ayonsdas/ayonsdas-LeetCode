/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @return Integer[]
     */
    function inorderTraversal($root) {
        $r = array();
        $this->traverse($root, $r);
        return $r;
    }
    
    function traverse($n, &$x)
    {
        if($n->left != null)
        {
            $this->traverse($n->left, $x);
        }
        array_push($x, $n->val);
        if($n->right != null)
        {
            $this->traverse($n->right, $x);
        }
    }
} 