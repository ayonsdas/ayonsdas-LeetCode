class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = [[0 for _ in matrix[0]] for _ in matrix]
        r = c = 0
        m = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        o = 0
        t = []
        for i in range(len(matrix) * len(matrix[0])):
            t.append(matrix[r][c])
            visited[r][c] = 1
            l = r + m[o][1]
            a = c + m[o][0]
            if l < 0 or l >= len(matrix) or a < 0 or a >= len(matrix[0]) or visited[l][a]:
                o = (o + 1) % 4
            r += m[o][1]
            c += m[o][0]
        return t