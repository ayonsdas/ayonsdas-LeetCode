from heapq import heappush, heappop, heapify

class MinHeap:
    
    def __init__(self):
        self.heap = []
        
    def parent(self, i: int) -> int:
        return (i - 1) // 2
    
    def addVal(self, val: int):
        heappush(self.heap, val)
    
    def updateKey(self, k: int, nVal: int) -> int:
        oVal = self.heap[k]
        self.heap[k] = new_val
        while k > 0 and self.heap[self.parent(k)] > self.heap[k]:
            self.heap[self.parent(k)], self.heap[k] = self.heap[k], self.heap[self.parent(k)]
            k = self.parent(k)
        return oVal
    
    def poll(self) -> int:
        return heappop(self.heap)
    
    def deleteKey(self, k) -> int:
        self.updateKey(k, -float("inf"))
        return self.poll()
    
    def peek(self) -> int:
        return self.heap[0]

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