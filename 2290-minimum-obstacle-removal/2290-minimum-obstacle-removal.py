import heapq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        edges = dict()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                edges[(i, j)] = []
                if i != 0:
                    edges[(i, j)].append(((i - 1, j), grid[i - 1][j]))
                if j != 0:
                    edges[(i, j)].append(((i, j - 1), grid[i][j - 1]))
                if i != m - 1:
                    edges[(i, j)].append(((i + 1, j), grid[i + 1][j]))
                if j != n - 1:
                    edges[(i, j)].append(((i, j + 1), grid[i][j + 1]))

        myQueue = []
        heapq.heappush(myQueue, (0, (0, 0)))
        visited = set()
        while myQueue:
            pair = heapq.heappop(myQueue)
            if pair[1] == (m - 1, n - 1):
                return pair[0]
            if pair[1] in visited:
                continue
            visited.add(pair[1])
            for successor in edges[pair[1]]:
                heapq.heappush(myQueue, (pair[0] + successor[1], successor[0]))
