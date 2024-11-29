class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        c = 0
        
        def finder(x: int, y: int) -> int:
            nonlocal grid1, grid2
            
            if x < 0 or x >= len(grid2) or y < 0 or y >= len(grid2[0]) or grid2[x][y] == 0:
                return 1
            
            if grid1[x][y] == 0:
                return 0
            
            grid2[x][y] = 0
            u, l, r, d = finder(x - 1, y), finder(x, y - 1), finder(x, y + 1), finder(x + 1, y)
            
            for a in [u, l, r, d]:
                if a == 0:
                    return 0
                
            return 2
        
        
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if finder(i, j) == 2:
                    c += 1
        
        return c