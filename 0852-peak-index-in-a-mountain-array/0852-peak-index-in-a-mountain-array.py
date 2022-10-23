class Solution:
    def peakIndexInMountainArray(self, a: List[int]) -> int:
        l = 0
        r = len(a) - 1
        while True:
            m = (l + r) // 2
            if a[m] > a[m + 1] and a[m] > a[m - 1]:
                return m
            elif a[m] < a[m + 1]:
                l = m + 1
            elif a[m] < a[m - 1]:
                r = m - 1