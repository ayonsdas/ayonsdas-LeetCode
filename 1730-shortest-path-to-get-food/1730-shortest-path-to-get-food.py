class Solution:
    def getFood(self, g: List[List[str]]) -> int:
        x = y = 0
        lg = len(g)
        lg2 = len(g[0])
        i = 0
        while i < lg:
            j = 0
            while j < lg2:
                if g[i][j] == "*":
                    x, y = i, j
                    break
                j += 1
            else:
                i += 1
                continue
            break
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        q = [(x, y)]
        r = 0
        while q:
            r += 1
            l = len(q)
            while l:
                l -= 1
                x, y = q.pop(0)
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy
                    
                    if nx < 0 or nx >= lg or ny < 0 or ny >= lg2:
                        continue
                        
                    if g[nx][ny] != "X":
                        if g[nx][ny] == "#":
                            return r
                        q.append((nx, ny))
                        g[nx][ny] = "X"
        return -1