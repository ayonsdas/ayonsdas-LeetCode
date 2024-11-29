# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        s = []
        def adder(rt: Optional[TreeNode]):
            if rt:
                adder(rt.left)
                s.append(rt.val)
                adder(rt.right)
        
        adder(root)
        return s[k - 1]