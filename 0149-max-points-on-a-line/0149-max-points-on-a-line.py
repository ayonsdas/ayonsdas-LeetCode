class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = 1
        
        def sl(i: int, j: int):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 - x2 == 0:
                return float('inf')
            return (y2 - y1) / (x2 - x1)
        
        for i in range(len(points)):
            s = defaultdict(int)
            for j in range(i + 1, len(points)):
                s[sl(i, j)] += 1
                m = max(m, s[sl(i, j)] + 1)
        return m