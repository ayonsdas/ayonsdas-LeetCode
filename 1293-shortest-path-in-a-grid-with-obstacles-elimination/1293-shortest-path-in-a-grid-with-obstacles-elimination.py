class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m = len(grid)
        n = len(grid[0])
        if k > m + n - 2:
            return m + n - 2
        
        dq = deque([(0, 0, k, 0)])
        
        cache = set()
        
        while dq:
            a = dq.popleft()
            if a[0] == m - 1 and a[1] == n - 1:
                return a[3]
            
            for x, y in [(a[0] - 1, a[1]), (a[0], a[1] - 1), (a[0] + 1, a[1]), (a[0], a[1] + 1)]:
                
                if x < 0 or y < 0 or x >= m or y >= n or (x, y, a[2] - grid[x][y]) in cache or a[2] < grid[x][y]:
                    continue
                    
                cache.add((x, y, a[2] - grid[x][y]))
                dq.append((x, y, a[2] - grid[x][y], a[3] + 1))
            
        return -1