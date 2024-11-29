class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r = [0 for _ in range(len(mat))]
        c = [0 for _ in range(len(mat[0]))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    r[i] += 1
                    c[j] += 1
        t = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    if r[i] == 1 and c[j] == 1:
                        t += 1
        return t