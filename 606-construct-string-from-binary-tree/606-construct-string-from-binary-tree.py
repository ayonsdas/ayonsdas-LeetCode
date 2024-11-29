# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ""
        t = str(root.val)
        if root.left != None:
            t += "(" + self.tree2str(root.left) + ")"
        if root.right != None:
            if root.left == None:
                t += "()"
            t += "(" + self.tree2str(root.right) + ")"
        return t