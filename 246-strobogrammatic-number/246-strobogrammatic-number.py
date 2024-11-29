class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        nums = {"6": "9", "1": "1", "9": "6", "8": "8", "0": "0"}
        for i in range(len(num) // 2 + 1):
            if not num[i] in nums:
                return False
            if num[~i] != nums[num[i]]:
                return False
        return True