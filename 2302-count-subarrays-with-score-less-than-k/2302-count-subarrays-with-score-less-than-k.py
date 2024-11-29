class Solution:
    def countSubarrays(self, n: List[int], k: int) -> int:
        c = 0
        s = 0
        l, r = 0, 0
        while r < len(n):
            s += n[r]
            
            while s * (r - l + 1) >= k:
                s -= n[l]
                l += 1
            
            c += (r - l + 1)
            r += 1
            
        return c