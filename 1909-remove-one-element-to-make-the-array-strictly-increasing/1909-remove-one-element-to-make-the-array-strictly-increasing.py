class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            nums2 = [l for l in nums]
            nums2.pop(i)
            for j in range(1, len(nums2)):
                if nums2[j] <= nums2[j - 1]:
                    break
            else:
                return True
        
        return False