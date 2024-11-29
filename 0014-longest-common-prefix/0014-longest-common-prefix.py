class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = ""
        for j in range(len(strs[0])):
            c = strs[0][j]
            for st in strs:
                if len(st) <= j or st[j] != c:
                    return p
            p += c
        return p