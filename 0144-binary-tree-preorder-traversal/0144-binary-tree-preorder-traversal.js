/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var preorderTraversal = function(root)
{
    var r = [];
    if(root == null)
    {
        return r;
    }
    traverse(root, r);
    return r;
};

var traverse = function(rt, r)
{
    r.push(rt.val);
    if(rt.left != null)
    {
        traverse(rt.left, r);
    }
    if(rt.right != null)
    {
        traverse(rt.right, r);
    }
};