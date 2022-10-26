class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        a = [num % k for num in nums]
        l = set()
        for i in range(1, len(nums)):
            a[i] += a[i - 1]
            a[i] %= k
            l.add(a[i - 2] if i >= 2 else 0)
            if a[i] in l:
                return True
        return False