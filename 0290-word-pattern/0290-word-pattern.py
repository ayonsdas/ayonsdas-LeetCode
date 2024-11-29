class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = {}
        n = {}
        pattern = [char for char in pattern]
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if not pattern[i] in m and not s[i] in n:
                m[pattern[i]] = s[i]
                n[s[i]] = pattern[i]
            elif not pattern[i] in m or not s[i] in n:
                return False
            else:
                if m[pattern[i]] != s[i] or n[s[i]] != pattern[i]:
                    return False
        return True