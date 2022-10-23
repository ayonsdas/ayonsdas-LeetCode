class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        md = 0
        for h in houses:
            l = 0
            r = len(heaters) - 1
            x1 = -1
            while l <= r:
                m = (l + r) // 2
                if heaters[m] == h or heaters[m] < h and (m == len(heaters) - 1 or heaters[m + 1] >= h):
                    x1 = m
                    break
                elif heaters[m] < h:
                    l = m + 1
                else:
                    r = m - 1
            if heaters[x1] == h or m < len(heaters) - 1 and heaters[m + 1] == h:
                continue
            x2 = (x1 + 1)
            a = (h - heaters[x1]) if x1 != -1 else float('inf')
            b = (heaters[x2] - h) if x2 != len(heaters) else float('inf')
            md = max(md, min(a, b))
        return md