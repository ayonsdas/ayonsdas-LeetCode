class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        x = [["." for _ in range(n)] for _ in range(n)]
        s = 0
        def safe(c: int, r: int):
            nonlocal n, x
            for i in range(c):
                for j in range(n):
                    if x[j][i] == "Q":
                        if j == r or i - j == c - r or i + j == c + r:
                            return False
                        break
            return True
        def finder(c: int):
            nonlocal x, n, s
            if c == n:
                s += 1
                return
            for i in range(n):
                x[i][c] = "Q"
                if safe(c, i):
                    finder(c + 1)
                x[i][c] = "."
        finder(0)
        return s