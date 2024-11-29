class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        m = 0
        l = r = 0
        while r < len(s):
            r += 1
            if s[r - 1] in a:
                while s[l] != s[r - 1]:
                    a.remove(s[l])
                    l += 1
                l += 1
            else:
                a.add(s[r - 1])
                m = max(m, r - l)
        return m