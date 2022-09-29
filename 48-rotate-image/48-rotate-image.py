class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        mL = len(m) // 2
        mX = len(m)
        while l < mL:
            a = 0
            while a < mX - 2 * l - 1:
                m[l][l + a], m[l + a][mX - l - 1], m[mX - l - 1][mX - l - a - 1], m[mX - l - a - 1][l] = m[mX - l - a - 1][l], m[l][l + a], m[l + a][mX - l - 1], m[mX - l - 1][mX - l - a - 1]
                a += 1
            l += 1