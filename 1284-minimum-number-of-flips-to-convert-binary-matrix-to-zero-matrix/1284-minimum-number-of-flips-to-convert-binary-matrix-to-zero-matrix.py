class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        c = 10
        p = len(mat) * len(mat[0])
        b = [0 for _ in range(p)]
        a = -1
        for i in range(2 ** p):
            d = []
            for t in mat:
                x = []
                for y in t:
                    x.append(y)
                d.append(x)
            for k in range(len(b)):
                if b[k] == 1:
                    m, n = k // len(mat[0]), k % len(mat[0])
                    d[m][n] += 1
                    if m > 0:
                        d[m - 1][n] += 1
                    if m < len(mat) - 1:
                        d[m + 1][n] += 1
                    if n > 0:
                        d[m][n - 1] += 1
                    if n < len(mat[0]) - 1:
                        d[m][n + 1] += 1
            for l in range(len(mat)):
                for s in range(len(mat[0])):
                    if (d[l][s] % 2) == 0:
                        continue
                    break
                else:
                    continue
                break
            else:
                if a == -1 or a > sum(b):
                    a = sum(b)
            j = 0
            while j < len(b) and b[~j] == 1:
                b[~j] = 0
                j += 1
            if j < len(b):
                b[~j] = 1
        return a