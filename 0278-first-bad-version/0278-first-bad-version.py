# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if r - l >= 2:
                if isBadVersion(m):
                    r = m
                else:
                    l = m
            else:
                if isBadVersion(m):
                    return m
                else:
                    return m + 1
        return l 