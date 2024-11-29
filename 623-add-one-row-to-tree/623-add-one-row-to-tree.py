# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            return TreeNode(val, root, None)
        q = [[root, 1]]
        while q:
            x = q.pop(0)
            if not x[0]:
                continue
            if x[1] + 1 == depth:
                x[0].left = TreeNode(val, x[0].left, None)
                x[0].right = TreeNode(val, None, x[0].right)
            else:
                q.append([x[0].left, x[1] + 1])
                q.append([x[0].right, x[1] + 1])
        
        return root