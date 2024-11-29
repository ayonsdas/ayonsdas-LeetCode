class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        x, y = 0, 0
        up = True
        a = []
        for i in range(len(mat) * len(mat[0])):
            a.append(mat[x][y])
            if up:
                if x == 0 or y == len(mat[0]) - 1:
                    if y < len(mat[0]) - 1:
                        y += 1
                    else:
                        x += 1
                    up = False
                else:
                    x -= 1
                    y += 1
            else:
                if y == 0 or x == len(mat) - 1:
                    if x < len(mat) - 1:
                        x += 1
                    else:
                        y += 1
                    up = True
                else:
                    x += 1
                    y -= 1
        return a