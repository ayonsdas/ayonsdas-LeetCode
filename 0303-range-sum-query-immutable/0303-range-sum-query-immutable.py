class NumArray:

    def __init__(self, nums: List[int]):
        self.x = [0]
        for i in range(len(nums)):
            self.x.append(self.x[-1] + nums[i])
        print(self.x)

    def sumRange(self, left: int, right: int) -> int:
        return self.x[right + 1] - self.x[left]


# Your NumArray object will be instantiated and called as such
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)