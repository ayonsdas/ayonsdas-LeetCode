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
        q = [(x, y, 0)]
        while q:
            x, y, l = q.pop(0)
            if x >= 0 and x < lg and y >= 0 and y < lg2 and g[x][y] != "X":
                if g[x][y] == "#":
                    return l
                for dx, dy in d:
                    q.append((x + dx, y + dy, l + 1))
                g[x][y] = "X"
        return -1