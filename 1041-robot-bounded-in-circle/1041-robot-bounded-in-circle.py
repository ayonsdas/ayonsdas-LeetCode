class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if (instructions.count("R") % 4) != (instructions.count("L") % 4):
            return True
        pos = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        p = 0
        x, y = 0, 0
        for char in instructions:
            if char == "L":
                p -= 1
                if p == -1:
                    p = 3
            elif char == "R":
                p = (p + 1) % 4
            else:
                x += pos[p][0]
                y += pos[p][1]
        return x == 0 and y == 0