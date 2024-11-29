class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        x = -1
        y = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x, y = i, j
                    break
            else:
                continue
            break
            
        def ffFinder(pX: int, pY: int) -> int:
            nonlocal grid
            if pX < 0 or pY < 0 or pX >= len(grid) or pY >= len(grid[0]) or grid[pX][pY] == -1:
                return 0
            if grid[pX][pY] == 2:
                for t in grid:
                    if 0 in t:
                        break
                else:
                    return 1
                return 0
            grid[pX][pY] = -1
            u = ffFinder(pX - 1, pY)
            d = ffFinder(pX + 1, pY)
            l = ffFinder(pX, pY - 1)
            r = ffFinder(pX, pY + 1)
            grid[pX][pY] = 0
            return u + d + l + r
        return ffFinder(x, y)