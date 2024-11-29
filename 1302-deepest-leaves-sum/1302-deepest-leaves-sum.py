# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stuff = []
        maxDepth = 0
        q = [[root, 0]]
        while q:
            t = q.pop(0)
            if t[0]:
                stuff.append([t[0].val, t[1]])
                maxDepth = max(maxDepth, t[1])
                q.append([t[0].left,  t[1] + 1])
                q.append([t[0].right, t[1] + 1])
        sus = 0
        for x in stuff:
            if x[1] == maxDepth:
                sus += x[0]
        return sus