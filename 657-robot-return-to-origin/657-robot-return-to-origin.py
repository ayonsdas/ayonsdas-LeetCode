class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for move in moves:
            x += 1 if move == "R" else -1 if move == "L" else 0
            y += 1 if move == "U" else -1 if move == "D" else 0
        return x == 0 and y == 0