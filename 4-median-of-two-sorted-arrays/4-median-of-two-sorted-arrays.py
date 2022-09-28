class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = []
        z = 0
        while nums1 or nums2:
            if not nums1:
                x.append(nums2.pop(-1))
            elif not nums2:
                x.append(nums1.pop(-1))
            else:
                if nums1[-1] > nums2[-1]:
                    x.append(nums1.pop(-1))
                else:
                    x.append(nums2.pop(-1))
            z += 1
        if z & 1:
            return float(x[z // 2])
        return float(x[z // 2] + x[z // 2 - 1]) / 2