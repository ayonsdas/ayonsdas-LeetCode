class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def finder(x, y):
            nonlocal grid
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            l = finder(x, y - 1)
            u = finder(x - 1, y)
            r = finder(x, y + 1)
            d = finder(x + 1, y)
            return 1 + l + u + r + d
        
        m = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                m = max(m, finder(i, j))
                
        return m