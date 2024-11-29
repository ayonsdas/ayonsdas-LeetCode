class Solution:
    def myAtoi(self, s: str) -> int:
        s = [char for char in s]
        i = 0
        total = 0
        negative = False
        active = False
        for i in range(len(s)):
            if not active:
                if ord(s[i]) >= 48 and ord(s[i]) <= 57:
                    active = True
                    total = int(s[i])
                elif ord(s[i]) == 43:
                    active = True
                elif ord(s[i]) == 45:
                    active = True
                    negative = True
                elif ord(s[i]) != 32:
                    break
                    
            elif ord(s[i]) < 48 or ord(s[i]) > 57:
                break
            else:
                total = total * 10 + int(s[i])
        if total >= 2 ** 31:
            total = 2 ** 31
            if not negative:
                total -= 1
        if negative:
            total *= -1
        return total