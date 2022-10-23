class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = sorted(heaters)
        md = 0
        for h in houses:
            l = 0
            r = len(heaters) - 1
            x1 = bisect.bisect(heaters, h)
            if x1 == 0:
                md = max(md, heaters[0] - h)
            elif x1 == len(heaters):
                md = max(md, h - heaters[-1])
            else:
                md = max(md, min(h - heaters[x1 - 1], heaters[x1] - h))
        return md