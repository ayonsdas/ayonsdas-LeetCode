"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        s = []
        q = [[root, 0]]
        l = -1
        while q:
            t = q.pop(0)
            if not t[0]:
                continue
            if t[1] > l:
                l = t[1]
                s.append([])
            s[-1].append(t[0].val)
            for a in t[0].children:
                q.append([a, t[1] + 1])
        return s