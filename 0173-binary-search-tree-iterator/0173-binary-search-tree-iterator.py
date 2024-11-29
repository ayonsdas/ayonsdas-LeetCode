# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = []
        self.adder(root)

    def adder(self, rt: Optional[TreeNode]):
        if not rt:
            return
        self.adder(rt.left)
        self.curr.append(rt.val)
        self.adder(rt.right)
        
    def next(self) -> int:
        return self.curr.pop(0)

    def hasNext(self) -> bool:
        return len(self.curr) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()