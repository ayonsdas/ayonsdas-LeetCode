# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stuff = []
        def trav(r: Optional[TreeNode]) -> None:
            if not r:
                return
            trav(r.left)
            trav(r.right)
            stuff.append(r.val)
        trav(root)
        return stuff