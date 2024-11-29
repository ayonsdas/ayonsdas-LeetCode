class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = Counter(nums1), Counter(nums2)
        t = []
        for l in nums1:
            if l in nums2:
                for i in range(min(nums1[l], nums2[l])):
                    t.append(l)
        return t