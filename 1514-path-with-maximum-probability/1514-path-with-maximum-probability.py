from heapq import heappop, heappush

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        go = defaultdict(list)
        for i in range(len(edges)):
            go[edges[i][0]].append([edges[i][1], -math.log10(succProb[i])])
            go[edges[i][1]].append([edges[i][0], -math.log10(succProb[i])])
        checked = set()
        q = []
        heappush(q, (0, start))
        while q:
            l = heappop(q)
            if l[1] == end:
                return 10 ** -l[0]
            if not l[1] in checked:
                checked.add(l[1])
                for a in go[l[1]]:
                    heappush(q, (a[1] + l[0], a[0]))
        return 0