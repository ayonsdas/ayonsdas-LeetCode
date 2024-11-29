# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        arr = []
        
        def inOrder(rt: TreeNode) -> None:
            
            nonlocal arr
            
            if rt:
                inOrder(rt.left)
                arr.append(rt)
                inOrder(rt.right)
                
        inOrder(root)
        
        for i in range(1, len(arr)):
            arr[~i].val += arr[-i].val
                
        return root