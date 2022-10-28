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
    fun inorderTraversal(root: TreeNode?): List<Int> {
        if(root == null)
            return mutableListOf();
        val s  = mutableListOf<Int>();
        for(a in inorderTraversal(root.left))
            s.add(a);
        s.add(root.`val`);
        for(a in inorderTraversal(root.right))
            s.add(a);
        return s;
    }
}