# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        
        if not root or not arr:
            return False

        if not arr[1:]:
            return root.val == arr[0] and not (root.left or root.right)
        
        l = self.isValidSequence(root.left,  arr[1:]) if (root.left  and root.left.val  == arr[1]) else False
        r = self.isValidSequence(root.right, arr[1:]) if (root.right and root.right.val == arr[1]) else False
        return l or r