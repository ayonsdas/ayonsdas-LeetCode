class Solution:
    def setZeroes(self, mx: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(mx)
        n = len(mx[0])
        r = False
        c = False
        for i in range(m):
            if mx[i][0] == 0:
                c = True
                break
        for j in range(n):
            if mx[0][j] == 0:
                r = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if mx[i][j] == 0:
                    mx[i][0] = 0
                    mx[0][j] = 0
        for i in range(1, m):
            if mx[i][0] == 0:
                for j in range(1, n):
                    mx[i][j] = 0
        for j in range(1, n):
            if mx[0][j] == 0:
                for i in range(1, m):
                    mx[i][j] = 0
        if mx[0][0] == 0:
            for i in range(1, m):
                mx[i][0] = 0
            for j in range(1, n):
                mx[0][j] = 0
        if r:
            for j in range(n):
                mx[0][j] = 0
        if c:
            for i in range(m):
                mx[i][0] = 0 