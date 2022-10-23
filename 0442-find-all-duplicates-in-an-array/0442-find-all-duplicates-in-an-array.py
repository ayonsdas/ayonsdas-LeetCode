class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        b = Counter(nums)
        a = []
        for l in b:
            if b[l] == 2:
                a.append(l)
        return a