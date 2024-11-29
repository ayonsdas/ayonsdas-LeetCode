# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.finder(root, [], 0, targetSum)
    
    def finder(self, root: Optional[TreeNode], currPath: List[int], currSum: int, targetSum: int) -> List[List[int]]:
        if root == None:
            return []
        t = []
        x = []
        for l in currPath:
            x.append(l)
        x.append(root.val)
        if currSum + root.val == targetSum and root.left == None and root.right == None:
            
            t.append(x)
            return t
        for z in self.finder(root.left, x, currSum + root.val, targetSum):
            t.append(z)
        for z in self.finder(root.right, x, currSum + root.val, targetSum):
            t.append(z)
        return t