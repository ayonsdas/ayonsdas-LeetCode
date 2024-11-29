from heapq import heappop, heappush

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = []
        for y in arr:
            if len(l) == k:
                if -abs(x - y) > l[0][0]:
                    heappushpop(l, (-abs(x - y), y))
            else:
                heappush(l, (-abs(x - y), y))
        return sorted([x[1] for x in l])