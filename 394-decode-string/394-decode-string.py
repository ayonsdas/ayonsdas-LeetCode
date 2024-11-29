class Solution:
    def decodeString(self, s: str) -> str:
        s1 = [1]
        s2 = [""]
        for i in range(len(s)):
            x = s[i]
            if ord(x) >= 48 and ord(x) <= 57:
                if i == 0 or ord(s[i - 1]) < 48 or ord(s[i - 1]) > 57:
                    s1.append(int(x))
                else:
                    s1[-1] *= 10
                    s1[-1] += int(x)
            elif x == "[":
                s2.append("")
            elif x == "]":
                for i in range(s1[-1]):
                    s2[-2] += s2[-1]
                s1.pop(-1)
                s2.pop(-1)
            else:
                s2[-1] += x
        return s2[0]