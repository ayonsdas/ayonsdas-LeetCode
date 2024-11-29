/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidSequence(TreeNode root, int[] arr) {
        return isValidHelper(root, arr, 0);
    }
    
    public boolean isValidHelper(TreeNode root, int[] arr, int pos) {
        if(root == null || pos >= arr.length)
            return false;
        
        if(pos == arr.length - 1)
            return root.val == arr[pos] && root.left == null && root.right == null;
        
        boolean l = (root.left  != null && root.left.val  == arr[pos + 1]) ? isValidHelper(root.left,  arr, pos + 1) : false;
        boolean r = (root.right != null && root.right.val == arr[pos + 1]) ? isValidHelper(root.right, arr, pos + 1) : false;
        return l || r;
    }
}