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
    public TreeNode InsertIntoBST(TreeNode root, int val) {
        if(root == null)
        {
            return new TreeNode(val);
        }
        TreeNode t = root;
        while(true)
        {
            if(val > t.val)
            {
                if(t.right == null)
                {
                    t.right = new TreeNode(val);
                    break;
                }
                else
                {
                    t = t.right;
                }
            }
            else
            {
                if(t.left == null)
                {
                    t.left = new TreeNode(val);
                    break;
                }
                else
                {
                    t = t.left;
                }
            }
        }
        return root;
    }
}