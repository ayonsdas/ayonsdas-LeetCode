class Solution {
    public int trapRainWater(int[][] hM) {
        if(hM == null || hM.length == 0 || hM[0] == null || hM[0].length == 0)
            return 0;
        int m = hM.length;
        int n = hM[0].length;
        
        if(m < 3 || n < 3)
            return 0;
        
        PriorityQueue<Integer[]> q = new PriorityQueue<>(new BruhComparator());
        
        for(int i = 0; i < m; i++)
        {
            q.offer(new Integer[] {hM[i][0], i, 0});
            q.offer(new Integer[] {hM[i][n - 1], i, n - 1});
            hM[i][0] = -1;
            hM[i][n - 1] = -1;
        }
        
        for(int j = 1; j < n - 1; j++)
        {
            q.offer(new Integer[] {hM[0][j], 0, j});
            q.offer(new Integer[] {hM[m - 1][j], m - 1, j});
            hM[0][j] = -1;
            hM[m - 1][j] = -1;
        }
        
        int r = 0, l = 0;
        int[][] dirs = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while(!q.isEmpty())
        {
            Integer[] a = q.poll();
            l = Math.max(l, a[0]);
            for(int[] dir : dirs)
            {
                int x = a[1] + dir[0];
                int y = a[2] + dir[1];
                if(x < 0 || y < 0 || x >= m || y >= n || hM[x][y] == -1)
                    continue;


                q.offer(new Integer[] {hM[x][y], x, y});

                if(hM[x][y] < l)
                    r += l - hM[x][y];                   

                hM[x][y] = -1;
            }
        }
        return r;
    }
}

class BruhComparator implements Comparator<Integer[]> {
    public int compare(Integer[] a, Integer[] b)
    {
        return a[0] - b[0];
    }
}

/*
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
*/