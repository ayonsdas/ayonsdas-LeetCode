class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        a = [num % k for num in nums]
        l = {}
        l[a[0]] = 0
        l[0] = -1
        for i in range(1, len(nums)):
            a[i] += a[i - 1]
            a[i] %= k
            if a[i] in l and l[a[i]] <= i - 2:
                return True
            if not a[i] in l:
                l[a[i]] = i
        print(a)
        return False