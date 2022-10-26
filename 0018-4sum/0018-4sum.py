class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k, l = j + 1, len(nums) - 1
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        a.add((nums[i], nums[j], nums[k], nums[l]))
                        l -= 1
                        k += 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                        l -= 1
                    else:
                        k += 1
        return a