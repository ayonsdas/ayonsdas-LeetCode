class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        keys = {}
        ans = []
        for num in nums:
            if not num in keys:
                keys[num] = 0
            keys[num] += 1
            if keys[num] == 2:
                ans.append(num)
        for i in range(len(nums)):
            if not i + 1 in keys:
                ans.append(i + 1)
                return ans