# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        c = 0
        def finder(rt: Optional[TreeNode]) -> int:
            nonlocal c
            if not rt.left and not rt.right:
                c += 1
                return rt.val
            l, r = rt.val, rt.val
            if rt.left:
                l = finder(rt.left)
            if rt.right:
                r = finder(rt.right)
            if rt.val == l and rt.val == r:
                c += 1
                return rt.val
            return -float('inf')
        if root:
            finder(root)
        return c