class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        cycs = [0 for _ in range(len(edges))]
        for i in range(len(edges)):
            j = 1
            t = i
            while cycs[t] == 0:
                if edges[t] == -1:
                    for x in visited:
                        cycs[x] = -1
                    cycs[t] = -1
                    break
                cycs[t] = ~j
                visited.add(t)
                t = edges[t]
                j += 1
            else:
                if cycs[t] == -1:
                    for x in visited:
                        cycs[x] = -1
                elif cycs[t] < 0:
                    for x in visited:
                        if x != t:
                            cycs[x] = j - ~cycs[t]
                    cycs[t] = j - ~cycs[t]
                else:
                    for x in visited:
                        cycs[x] = cycs[t]
            visited = set()
        return max(cycs)