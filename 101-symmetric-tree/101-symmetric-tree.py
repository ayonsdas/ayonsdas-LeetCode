# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or not root.left and not root.right:
            return True
        q1 = [root.left]
        q2 = [root.right]
        while q1 and q2:
            s1 = q1.pop(-1)
            s2 = q2.pop(-1)
            if s1 == None and s2 == None:
                continue
            if s1 != s2 and (s1 == None or s2 == None):
                return False
            if s1.val != s2.val:
                return False
            q1.append(s1.right)
            q1.append(s1.left)
            q2.append(s2.left)
            q2.append(s2.right)
        return True