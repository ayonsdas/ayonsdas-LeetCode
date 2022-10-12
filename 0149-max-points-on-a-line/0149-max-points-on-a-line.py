class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = 1
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                c = 2
                rise = points[j][1] - points[i][1]
                run = points[j][0] - points[i][0]
                u = (run != 0)
                b = 0
                if u:
                    b = points[j][1] * run - points[j][0] * rise
                for k in range(len(points)):
                    if k != i and k != j:
                        if u:
                            if points[k][0] * rise + b == points[k][1] * run:
                                c += 1
                        else:
                            if points[k][0] == points[i][0]:
                                c += 1
        
                m = max(m, c)
        return m