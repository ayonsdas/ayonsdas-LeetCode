class Solution {
    
    private Set<Cell> visited = new HashSet<>();
    private int m, n;
    private int[][] dirs = new int[][] { {0,1}, {1,0}, {0,-1}, {-1,0} };
    
    public int shortestPath(int[][] g, int k) {
        this.m = g.length; this.n = g[0].length;
        
        if (k >= m + n - 2) return m + n - 2;
        
        var q = new ArrayDeque<Cell>();
        int steps = 0;
        
        q.add(new Cell(0,0, g[0][0]));
        
        while (!q.isEmpty()) {
            int size = q.size();
            
            for (int i = 0; i < size; i++) {
                var c = q.poll();
                if (c.x == m-1 && c.y == n-1) return steps;
                
                if (g[c.x][c.y] == 1) {
                    c.obs++;
                    if (c.obs > k) continue;
                }
                
                for (var dir : dirs) {
                    int x1 = c.x + dir[0], y1 = c.y + dir[1]; 
                    
                    if (isOutOfBounds(x1,y1)) continue;
                    
                    Cell neighbor = new Cell(x1, y1, c.obs);
                    if (!visited.contains(neighbor)) {
                        q.offer(neighbor);
                        visited.add(neighbor);
                    }
                }
            }
            steps++;
        }
        return -1;
    }
    
    private boolean isOutOfBounds(int x, int y) {
        return x < 0 || x == m || y < 0 || y == n;
    }
    
    private static class Cell {
        int x, y, obs;
        
        private Cell(int x, int y, int obs) {
            this.x = x; this.y = y; this.obs = obs;
        }

        @Override
        public String toString() {
            return "(" + x + "," + y + "," + obs + ")";
        }
        
        @Override
        public boolean equals(Object o) {
            if (o == null || !(o instanceof Cell)) return false;
            Cell c = (Cell) o;
            return this.x == c.x && this.y == c.y && this.obs == this.obs;
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(this.x, this.y, this.obs);
        }
    }
}