class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[~i])):
                triangle[~i][j] += min(triangle[-i][j], triangle[-i][j + 1])
        
        return triangle[0][0]