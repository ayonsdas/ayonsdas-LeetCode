class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        length = len(nums1) + len(nums2)
        half = length // 2
        l, r = 0, len(nums1) - 1
        
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            l1 = nums1[i] if i >= 0 else float('-inf')
            r1 = nums1[i + 1] if i < len(nums1) - 1 else float('inf')
            l2 = nums2[j] if j >= 0 else float('-inf')
            r2 = nums2[j + 1] if j < len(nums2) - 1 else float('inf')
            if l1 <= r2 and l2 <= r1:
                if length % 2:
                    return float(min(r1, r2))
                return (min(r1, r2) + max(l1, l2)) / 2
            if l1 > r2:
                r = i - 1
            else:
                l = i + 1