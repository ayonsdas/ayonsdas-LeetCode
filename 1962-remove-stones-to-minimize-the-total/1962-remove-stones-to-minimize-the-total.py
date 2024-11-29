from heapq import heappush, heappop, heapify

class MinHeap:
    
    def __init__(self):
        self.heap = []
    
    def addVal(self, val: int):
        heappush(self.heap, val)
    
    def poll(self) -> int:
        return heappop(self.heap)

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        t = sum(piles)
        h = MinHeap()
        for pile in piles:
            h.addVal(-pile)
        for i in range(k):
            s = -h.poll()
            t -= (s // 2)
            s -= (s // 2)
            h.addVal(-s)
        return t