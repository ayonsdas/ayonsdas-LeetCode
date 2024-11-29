import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[1][0] >= 2 and grid[0][1] >= 2:
            return -1
        myQueue = []
        heapq.heappush(myQueue, (0, (0, 0)))
        visited = set()
        while heapq:
            pair = heapq.heappop(myQueue)
            if pair[1] == (m - 1, n - 1):
                return pair[0]
            if pair[1] in visited:
                continue
            visited.add(pair[1])
            for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = pair[1][0] + delta[0]
                y = pair[1][1] + delta[1]
                if x >= 0 and y >= 0 and x < m and y < n:
                    heapq.heappush(myQueue, (max(pair[0] + 1, grid[x][y] + (1 if (grid[x][y] & 1 == pair[0] & 1) else 0)), (x, y)))


