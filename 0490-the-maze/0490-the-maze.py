class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], d: List[int]) -> bool:
        q = [(start[0], start[1])]
        v = set()
        while q:
            m = q.pop(0)
            if (m[0], m[1]) in v:
                continue
            if (m[0], m[1]) == (d[0], d[1]):
                return True
            v.add((m[0], m[1]))
            x, y = m[0], m[1]
            while x > 0 and not maze[x - 1][y]:
                x -= 1
            q.append((x, y))
            
            x, y = m[0], m[1]
            while y > 0 and not maze[x][y - 1]:
                y -= 1
            q.append((x, y))
            
            x, y = m[0], m[1]
            while x < len(maze) - 1 and not maze[x + 1][y]:
                x += 1
            q.append((x, y))
            
            x, y = m[0], m[1]
            while y < len(maze[0]) - 1 and not maze[x][y + 1]:
                y += 1
            q.append((x, y))
            
        return False