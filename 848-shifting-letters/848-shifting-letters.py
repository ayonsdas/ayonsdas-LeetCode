class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = [ord(c) for c in s]
        l = [0]
        for shift in shifts[::-1]:
            l.append(l[-1] + shift)
            l[-1] %= 26
        for i in range(len(s)):
            s[i] += l[~i]
            if s[i] > 122:
                s[i] -= 26
        return "".join([chr(c) for c in s])