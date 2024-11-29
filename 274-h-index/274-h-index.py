class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cSort = [0] * 1001
        for cit in citations:
            cSort[cit] += 1
        for i in range(1, 1001):
            cSort[i] += cSort[i - 1]
        for i in range(1001):
            if len(citations) - cSort[i] <= i:
                return i