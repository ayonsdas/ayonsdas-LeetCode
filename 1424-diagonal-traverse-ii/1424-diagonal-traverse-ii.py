class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        x = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                x.append((i, j, nums[i][j]))
        return [a[2] for a in sorted(sorted(x, key = lambda a : a[1]), key = lambda a : a[0] + a[1])]