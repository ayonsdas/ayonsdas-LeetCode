class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        c = inf
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(c - target) > abs(s - target):
                    c = s
                
                m = (l + r) // 2
                    
                if s > target:
                    if m != r and nums[m] > (target - nums[i] - nums[l]):
                        r = m
                    else:
                        r -= 1
                elif s < target:
                    if m != l and nums[m] < (target - nums[i] - nums[r]):
                        l = m
                    else:
                        l += 1
                else:
                    return target
        return c