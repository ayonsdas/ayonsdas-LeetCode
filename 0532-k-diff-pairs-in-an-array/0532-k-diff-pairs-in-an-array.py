class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        a = set()
        c = set()
        for i in range(len(nums)):
            if nums[i] - k in a:
                c.add((nums[i] - k, nums[i]))
            if nums[i] + k in a:
                c.add((nums[i], nums[i] + k))
            a.add(nums[i])
        return len(list(c))