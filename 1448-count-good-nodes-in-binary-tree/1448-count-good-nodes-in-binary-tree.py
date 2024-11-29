# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        c = 0
        s = [[root, -float('inf')]]
        while s:
            t = s.pop(-1)
            if not t[0]:
                continue
            if t[0].val >= t[1]:
                c += 1
            s.append([t[0].left, max(t[0].val, t[1])])
            s.append([t[0].right, max(t[0].val, t[1])])
        return c