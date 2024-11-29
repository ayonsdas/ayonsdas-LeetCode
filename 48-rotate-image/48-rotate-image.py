class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        while l < len(m) // 2:
            a = 0
            while a < len(m) - 2 * l - 1:
                m[l][l + a], m[l + a][len(m) - l - 1], m[len(m) - l - 1][len(m) - l - a - 1], m[len(m) - l - a - 1][l] = m[len(m) - l - a - 1][l], m[l][l + a], m[l + a][len(m) - l - 1], m[len(m) - l - 1][len(m) - l - a - 1]
                a += 1
            l += 1