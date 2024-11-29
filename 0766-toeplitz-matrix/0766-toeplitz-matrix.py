class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix) - 1
        n = 0
        for i in range(len(matrix) + len(matrix[0]) - 1):
            
            x = m
            y = n
            val = matrix[x][y]
            while x < len(matrix) and y < len(matrix[0]):
                if matrix[x][y] != val:
                    return False
                x += 1
                y += 1
            
            if m > 0:
                m -= 1
            else:
                n += 1
        return True