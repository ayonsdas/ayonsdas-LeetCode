class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        a = set()
        for x, y in obstacles:
            a.add((x, y))
        x = y = p = r = 0
        for i in range(len(commands)):
            if commands[i] == -1:
                r = (r + 1) % 4
            elif commands[i] == -2:
                r = (r + 3) % 4
            else:
                for j in range(commands[i]):
                    if (x + d[r][0], y + d[r][1]) in a:
                        break
                    else:
                        x += d[r][0]
                        y += d[r][1]
                p = max(p, x ** 2 + y ** 2)
        return p