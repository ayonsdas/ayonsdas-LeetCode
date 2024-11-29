class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mi, ma = 0, len(matrix) - 1
        while True:
            if mi > ma:
                return False
            r = (mi + ma) // 2
            if target > matrix[r][-1]:
                mi = r + 1
            elif target < matrix[r][0]:
                ma = r - 1
            else:
                break
        r = (mi + ma) // 2
        mi, ma = 0, len(matrix[r]) - 1
        while True:
            if mi > ma:
                return False
            c = (mi + ma) // 2
            if target > matrix[r][c]:
                mi = c + 1
            elif target < matrix[r][c]:
                ma = c - 1
            else:
                return True