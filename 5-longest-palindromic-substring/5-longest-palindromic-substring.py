class Solution:
    def longestPalindrome(self, s: str) -> str:
        returnable = ""
        for i in range(len(s)):
            for r in range(2):
                x = i
                y = i + r
                while x >= 0 and y < len(s):
                    if s[x] != s[y]:
                        break
                    if y - x + 1 > len(returnable):
                        returnable = s[x : y + 1]
                    x -= 1
                    y += 1
        return returnable