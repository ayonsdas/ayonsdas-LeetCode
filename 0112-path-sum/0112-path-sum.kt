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
class Zip(var `r` : TreeNode?, var `h` : Int)
{
    
}

class Solution {
    fun hasPathSum(root: TreeNode?, targetSum: Int): Boolean {
        var s = LinkedList<Zip>();
        s.add(Zip(root, 0));
        while(s.size > 0)
        {
            var t : Zip = s.removeAt(s.size - 1);
            if(t.r != null)
            {
                var a : TreeNode? = t.r;
                if(a!!.`val` + t.h == targetSum && a.left == null && a.right == null)
                {
                    return true;
                }
                s.add(Zip(a.left, t.h + a!!.`val`));
                s.add(Zip(a.right, t.h + a!!.`val`));
            }
        }
        return false;
    }
}


/**


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        q = [[root, 0]]
        while q:
            t = q.pop(-1)
            if t[0]:
                if t[0].val + t[1] == targetSum and not t[0].left and not t[0].right:
                    return True
                q.append([t[0].left,  t[1] + t[0].val])
                q.append([t[0].right, t[1] + t[0].val])
        return False
        
*/