class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        count = collections.Counter(digits)
        
        mod1 = count[1] + count[4] + count[7]
        zeroMod1 = not mod1
        mod1 %= 3
        
        mod2 = count[2] + count[5] + count[8]
        zeroMod2 = not mod2
        mod2 %= 3
        
        nums1, nums2 = (1, 4, 7), (2, 5, 8)
        
        def removeK(nums, k):
            for i in nums:
                rem = min(count[i], k)
                count[i] -= rem
                k -= rem  
        
        if mod1 == mod2:
            removeK((), 0)
        elif zeroMod1:
            removeK(nums2, mod2)
        elif zeroMod2:
            removeK(nums1, mod1)
        elif (mod1 - mod2) % 3 == 1:
            removeK(nums1, 1)
        else:
            removeK(nums2, 1)
        
        res = ''.join(str(digit) * count[digit] for digit in range(9, -1, -1))
        return res if not res or res[0] != '0' else '0'