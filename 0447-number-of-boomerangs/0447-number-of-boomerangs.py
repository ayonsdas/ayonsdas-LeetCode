class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        c = 0
        for x1, y1 in points:
            m = defaultdict(int)
            for x2, y2 in points:
                m[(x2 - x1) ** 2 + (y2 - y1) ** 2] += 1
            for a in m:
                c += m[a] * (m[a] - 1)
        return c