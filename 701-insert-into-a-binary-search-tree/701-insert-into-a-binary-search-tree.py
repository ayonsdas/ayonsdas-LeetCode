# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val, None, None)
        t = root
        while True:
            if val > t.val:
                if t.right == None:
                    t.right = TreeNode(val, None, None)
                    break
                else:
                    t = t.right
            else:
                if t.left == None:
                    t.left = TreeNode(val, None, None)
                    break
                else:
                    t = t.left
        return root