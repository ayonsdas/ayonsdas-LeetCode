class Solution:
    def maxPower(self, s: str) -> int:
        t = 1
        r = [1]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                r.append(r[-1] + 1)
            else:
                r.append(1)
            t = max(t, r[-1])
        return t