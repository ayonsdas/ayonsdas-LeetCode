class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        keys = {}
        xMin = float('inf')
        xMax = -float('inf')
        for point in points:
            if point[0] > xMax:
                xMax = point[0]
            if point[0] < xMin:
                xMin = point[0]
            if not point[1] in keys:
                keys[point[1]] = set()
            keys[point[1]].add(point[0])
        ref = (xMin + xMax) / 2
        for point in points:
            if not point[0] + 2 * (ref - point[0]) in keys[point[1]]:
                return False
        return True