from heapq import heapify, heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = []
        for num in nums:
            heappush(a, -num)
        for i in range(k - 1):
            heappop(a)
        return -heappop(a)