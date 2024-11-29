# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        s = []
        q = [[root, 0]]
        r = 0
        t = []
        while q:
            m = q.pop(0)
            if m[1] == r:
                if m[0]:
                    t.append(m[0].val)
            else:
                if r % 2:
                    s.append(t[::-1])
                else:
                    s.append(t)
                t = []
                if m[0]:
                    t.append(m[0].val)
                r += 1
            if m[0]:
                q.append([m[0].left,  m[1] + 1])
                q.append([m[0].right, m[1] + 1])
        return s