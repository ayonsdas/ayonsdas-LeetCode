class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        c = 0
        def finder(x: int, y: int):
            nonlocal grid, c
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == "0":
                return
            grid[x][y] = "0"
            t = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for a, b in t:
                finder(x + a, y + b)
            return True
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if finder(i, j):
                    c += 1
        return c