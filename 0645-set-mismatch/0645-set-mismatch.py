class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        keys = Counter(nums)
        ans = [-1, -1]
        for i in range(len(nums)):
            if not i + 1 in keys:
                ans[1] = i + 1
                if not -1 in ans:
                    return ans
            if keys[i + 1] == 2:
                ans[0] = i + 1
                if not -1 in ans:
                    return ans