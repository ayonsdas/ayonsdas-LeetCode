# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        a = set()
        q = [root]
        while q:
            t = q.pop(-1)
            if not t:
                continue
            if k - t.val in a:
                return True
            a.add(t.val)
            q.append(t.left)
            q.append(t.right)
            
        return False