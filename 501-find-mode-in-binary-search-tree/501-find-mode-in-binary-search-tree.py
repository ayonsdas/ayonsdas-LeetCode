# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        key = {}
        q = [root]
        while q:
            l = q.pop(-1)
            if not l:
                continue
            q.append(l.left)
            q.append(l.right)
            if not l.val in key:
                key[l.val] = 0
            key[l.val] += 1
        a = list(sorted(key.keys(), key = lambda x : key[x], reverse = True))
        v = key[a[0]]
        r = []
        i = 0
        while i < len(a) and key[a[i]] == v:
            r.append(a[i])
            i += 1
        return r