/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public bool IsValidSequence(TreeNode root, int[] arr) {
        return isValidHelper(root, arr, 0);
    }

    public bool isValidHelper(TreeNode root, int[] arr, int pos) {
        if(root == null || pos >= arr.Length)
            return false;

        if(pos == arr.Length - 1)
            return root.val == arr[pos] && root.left == null && root.right == null;

        bool l = (root.left  != null && root.left.val  == arr[pos + 1]) ? isValidHelper(root.left,  arr, pos + 1) : false;
        bool r = (root.right != null && root.right.val == arr[pos + 1]) ? isValidHelper(root.right, arr, pos + 1) : false;
        return l || r;
    }
}