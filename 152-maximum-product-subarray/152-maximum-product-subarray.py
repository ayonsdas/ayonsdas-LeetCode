class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cp = 1
        cn = 1
        mxp = max(nums)
        for num in nums:
            if num == 0:
                cp, cn = 1, 1
            else:
                t = cp * num
                cp = max(t, cn * num, num)
                cn = min(t, cn * num, num)
                mxp = max(mxp, cp, cn)
        return mxp