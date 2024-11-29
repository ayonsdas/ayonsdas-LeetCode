/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun preorderTraversal(root: TreeNode?): List<Int> {
        if(root == null)
            return mutableListOf();
        val s  = mutableListOf<Int>();
        s.add(root.`val`);
        for(a in preorderTraversal(root.left))
            s.add(a);
        for(a in preorderTraversal(root.right))
            s.add(a);
        return s;
    }
}