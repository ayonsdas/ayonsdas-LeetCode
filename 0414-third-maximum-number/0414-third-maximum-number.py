class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = sorted(list(dict.fromkeys(nums)), reverse = True)
        if len(a) >= 3:
            return a[2]
        return a[0]