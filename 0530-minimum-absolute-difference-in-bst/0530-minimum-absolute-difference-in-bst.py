# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l = []
        def adder(rt):
            if not rt:
                return
            adder(rt.left)
            l.append(rt.val)
            adder(rt.right)
        adder(root)
        m = float('inf')
        for i in range(1, len(l)):
            m = min(m, l[i] - l[i - 1])
        return m