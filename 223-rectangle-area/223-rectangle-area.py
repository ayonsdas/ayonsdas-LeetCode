class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a = (min(ay2, by2) - max(ay1, by1)) * (min(ax2, bx2) - max(ax1, bx1))
        if ax1 >= bx2 or bx1 >= ax2 or ay1 >= by2 or by1 >= ay2:
            a = 0
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - a