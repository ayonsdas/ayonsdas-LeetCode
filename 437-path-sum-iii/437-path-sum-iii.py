# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path = []
        c = 0
        def finder(r: Optional[TreeNode], rSum: int):
            nonlocal path, c
            if not r:
                return
            if r.val == rSum:
                c += 1
            finder(r.left,  rSum - r.val)
            finder(r.right, rSum - r.val)
        q = [root]
        while q:
            t = q.pop(-1)
            if t != None:
                q.append(t.left)
                q.append(t.right)
                finder(t, targetSum)
        return c