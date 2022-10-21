class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in a and abs(a[nums[i]] - i) <= k:
                return True
            a[nums[i]] = i
        return False