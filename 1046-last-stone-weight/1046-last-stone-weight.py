from heapq import heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        x = []
        for stone in stones:
            heappush(x, -stone)
            
        while len(x) > 1:
            a = -heappop(x)
            b = -heappop(x)
            if a != b:
                heappush(x, b - a)
            
        return -heappop(x) if x else 0