# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        q = [[root, 0]]
        while q:
            t = q.pop(-1)
            if t[0]:
                if t[0].val + t[1] == targetSum and not t[0].left and not t[0].right:
                    return True
                q.append([t[0].left,  t[1] + t[0].val])
                q.append([t[0].right, t[1] + t[0].val])
        return False