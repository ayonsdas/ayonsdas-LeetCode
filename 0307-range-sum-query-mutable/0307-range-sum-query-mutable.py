class NumArray:

    def __init__(self, nums: List[int]):
        self.bit = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.update(i, nums[i])

    def update(self, i: int, val: int) -> None:
        d = val - (self.rangeSum(i) - self.rangeSum(i - 1))
        if d != 0:
            self.up(i, d)
        
    def up(self, i: int, d: int) -> None:
        i += 1
        while i < len(self.bit):
            self.bit[i] += d
            i += i & -i

    def sumRange(self, left: int, right: int) -> int:
        return self.rangeSum(right) - self.rangeSum(left - 1)
    
    def rangeSum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)