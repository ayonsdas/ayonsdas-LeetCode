# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        a = root.val
        def finder(r: Optional[TreeNode]):
            nonlocal a
            if r == None:
                return 0
            x = max(finder(r.left),  0)
            y = max(finder(r.right), 0)
            a = max(a, x + y + r.val)
            return r.val + max(x, y)
            
        finder(root)
        return a