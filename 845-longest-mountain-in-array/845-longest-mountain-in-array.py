class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        dp =  [0 for c in arr]
        dp2 = [0 for c in arr]
        c1 = 0
        c2 = 0
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i - 1]:
                c1 += 1
            else:
                c1 = 0
            if arr[~i] > arr[-i]:
                c2 += 1
            else:
                c2 = 0
            dp[i]   = c1
            dp2[~i] = c2
        for i in range(1, len(arr)-1):
            if dp[i] == 0 or dp2[i] == 0:
                dp[i] = 0
            else:
                dp[i] += dp2[i] + 1
        return max(dp)