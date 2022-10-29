from heapq import heappush as h, heappop as p

class Solution:
    def trapRainWater(self, hM: List[List[int]]) -> int:
        if not hM or not hM[0]:
            return 0
        
        m = len(hM)
        n = len(hM[0])
        
        if m < 3 or n < 3:
            return 0
        
        q = []
        
        for i in range(m):
            h(q, (hM[i][0], i, 0))
            h(q, (hM[i][n - 1], i, n - 1))
            hM[i][0] = -1
            hM[i][n - 1] = -1
            
        for j in range(1, n - 1):
            h(q, (hM[0][j], 0, j))
            h(q, (hM[m - 1][j], m - 1, j))
            hM[0][j] = -1
            hM[m - 1][j] = -1
            
        r = l = 0
        while q:
            a, b, c = p(q)
            l = max(a, l)
            for x, y in [(b - 1, c), (b + 1, c), (b, c - 1), (b, c + 1)]:
                if x < 0 or x >= m or y < 0 or y >= n or hM[x][y] == -1:
                    continue
                
                h(q, (hM[x][y], x, y))
                
                if hM[x][y] < l:
                    r += l - hM[x][y]
                
                hM[x][y] = -1
                
        return r