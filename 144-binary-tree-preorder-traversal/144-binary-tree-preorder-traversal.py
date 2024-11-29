# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stuff = []
        def trav(r: Optional[TreeNode]) -> None:
            if not r:
                return
            stuff.append(r.val)
            trav(r.left)
            trav(r.right)
        trav(root)
        return stuff