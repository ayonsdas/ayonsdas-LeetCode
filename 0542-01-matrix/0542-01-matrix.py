class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        v = set()
        q = []
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
        while q:
            m = q.pop(0)
            if not (m[0], m[1]) in v and m[0] >= 0 and m[0] < len(mat) and m[1] >= 0 and m[1] < len(mat[0]):
                mat[m[0]][m[1]] = m[2]
                for x, y in d:
                    q.append((m[0] + x, m[1] + y, m[2] + 1))
                v.add((m[0], m[1]))
        return mat