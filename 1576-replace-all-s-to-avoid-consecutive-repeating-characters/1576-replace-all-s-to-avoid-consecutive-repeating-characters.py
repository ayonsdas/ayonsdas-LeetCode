class Solution:
    def modifyString(self, s: str) -> str:
        s = [char for char in s]
        if len(s) == 1 and s[0] == "?":
            return "a"
        for i in range(len(s)):
            if s[i] == "?":
                if i > 0 and i < len(s) - 1:
                    if s[i - 1] == "a" and s[i + 1] == "b" or s[i - 1] == "b" and s[i + 1] == "a":
                        s[i] = "c"
                    elif s[i - 1] == "a" or s[i + 1] == "a":
                        s[i] = "b"
                    else:
                        s[i] = "a"
                elif i == 0:
                    if s[1] == "a":
                        s[0] = "b"
                    else:
                        s[0] = "a"
                else:
                    if s[~1] == "a":
                        s[~0] = "b"
                    else:
                        s[~0] = "a"
        return "".join(s)