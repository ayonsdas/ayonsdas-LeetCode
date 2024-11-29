class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {}
        for edge in edges:
            x = edge[0]
            y = edge[1]
            if x in parents and y in parents:
                while x != parents[x]:
                    x = parents[x]
                while y != parents[y]:
                    y = parents[y]
                if x == y:
                    return edge
            if x in parents:
                parents[y] = x
            elif y in parents:
                parents[x] = y
            else:
                parents[x] = x
                parents[y] = x