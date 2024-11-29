class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = Counter(nums[::2])
        r = Counter(nums[1::2])
        s = sorted(l.keys(), key = lambda x : l[x], reverse = True)
        t = sorted(r.keys(), key = lambda x : r[x], reverse = True)
        if len(t) == 0:
            return 0
        if s[0] != t[0]:
            return len(nums) - l[s[0]] - r[t[0]]
        return min(len(nums) - (l[s[1]] if len(s) > 1 else 0) - r[t[0]], len(nums) - (r[t[1]] if len(t) > 1 else 0) - l[s[0]])