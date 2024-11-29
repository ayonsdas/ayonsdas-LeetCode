class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        tails = []
        for num in nums:
            if len(tails) == 0 or num > tails[-1]:
                tails.append(num)
            elif num < tails[0]:
                tails[0] = num
            else:
                r = len(tails) - 1
                l = -1
                while r - l > 1:
                    m = (l + r) // 2
                    if tails[m] < num:
                        l = m
                    else:
                        r = m
                tails[r] = num
        return len(tails)