class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        c = {}
        def finder(pos: int, s: int):
            nonlocal nums, target
            if (pos, s) in c:
                return c[(pos, s)]
            if pos == len(nums):
                c[(pos, s)] = 1 if s == target else 0
                return c[(pos, s)]
            c[(pos, s)] = finder(pos + 1, s + nums[pos]) + finder(pos + 1, s - nums[pos])
            return c[(pos, s)]
        return finder(0, 0)