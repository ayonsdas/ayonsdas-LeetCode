class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        return sorted(nums.keys(), key = lambda x: -nums[x])[:k]