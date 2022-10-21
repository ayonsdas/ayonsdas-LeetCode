class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        x = 0
        mx = len(mat)
        my = len(mat[0])
        while x < mx:
            y = 0
            while y < my:
                if mat[x][y]:
                    u = mat[x - 1][y] + 1 if x > 0 else float('inf')
                    l = mat[x][y - 1] + 1 if y > 0 else float('inf')
                    mat[x][y] = min(u, l)
                y += 1
            x += 1
        x = mx - 1
        while x >= 0:
            y = my - 1
            while y >= 0:
                if mat[x][y]:
                    d = mat[x + 1][y] + 1 if x < mx - 1 else float('inf')
                    r = mat[x][y + 1] + 1 if y < my - 1 else float('inf')
                    mat[x][y] = min(mat[x][y], d, r)
                y -= 1
            x -= 1
        return mat