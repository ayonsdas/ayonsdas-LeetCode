class Solution {
    
    Set<Zip> cache = new HashSet<>();
    int m, n;
    int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    
    public int shortestPath(int[][] grid, int k) {
        
        m = grid.length; n = grid[0].length;
        
        if(k >= m + n - 2)
        {
            return m + n - 2;
        }
        
        var dq = new ArrayDeque<Zip>(); 
        
        dq.add(new Zip(0, 0, grid[0][0]));
        int s = 0;
        
        while(!dq.isEmpty())
        {
            int c = dq.size();
            
            for(int i = 0; i < c; i++)
            {
                Zip a = dq.poll();

                if(a.x == m - 1 && a.y == n - 1)
                {
                    return s;
                }
                
                if(grid[a.x][a.y] == 1)
                {
                    a.k++;
                    if(a.k > k)
                        continue;
                }

                for(int[] dir : dirs)
                {
                    int x = a.x + dir[0], y = a.y + dir[1];

                    if(x < 0 || y < 0 || x >= m || y >= n)
                        continue;

                    Zip b = new Zip(x, y, a.k);

                    if(!cache.contains(b))
                    {
                        cache.add(b);
                        dq.offer(b);
                    }
                }
            }
            s++;
        }
        
        return -1;
    }
    
    private class Zip {
    
        int x;
        int y;
        int k;

        private Zip(int x, int y, int k)
        {
            this.x = x;
            this.y = y;
            this.k = k;
        }

        @Override
        public boolean equals(Object o)
        {   
            Zip zO = (Zip) o;

            return this.x == zO.x && this.y == zO.y && this.k == zO.k;
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(this.x, this.y, this.k);
        }

    }
}