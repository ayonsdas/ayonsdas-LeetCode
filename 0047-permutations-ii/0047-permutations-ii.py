from itertools import permutations as p

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        return list(set(permutations(nums)))