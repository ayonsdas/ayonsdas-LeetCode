class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        t = 0
        for i in range(len(mat)):
            t += mat[i][i] + mat[i][~i]
        if len(mat) & 1:
            t -= mat[len(mat)//2][len(mat)//2]
        return t