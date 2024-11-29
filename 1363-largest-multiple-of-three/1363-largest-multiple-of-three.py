class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits = sorted(digits, reverse = True)
        t = sum(digits)
        if t == 0:
            if len(digits) == 0:
                return ""
            return "0"
        if t % 3 == 0:
            return "".join(map(str, digits))
        mod0 = []
        mod1 = []
        mod2 = []
        for digit in digits:
            if digit % 3 == 0:
                mod0.append(digit)
            elif digit % 3 == 1:
                mod1.append(digit)
            else:
                mod2.append(digit)
        if t % 3 == 1:
            if len(mod1) >= 1:
                t -= mod1[-1]
                mod1.pop(-1)
            elif len(mod2) >= 2:
                t -= mod2[-1] + mod2[-2]
                mod2.pop(-1)
                mod2.pop(-1)
            else:
                return ""
        else:
            if len(mod2) >= 1:
                t -= mod2[-1]
                mod2.pop(-1)
            elif len(mod1) >= 2:
                t -= mod1[-1] + mod1[-2]
                mod1.pop(-1)
                mod1.pop(-1)
            else:
                return ""
        x = ""
        if t == 0:
            if mod0:
                return "0"
            return ""
        while mod0 or mod1 or mod2:
            if not mod1 and not mod2:
                x += str(mod0[0])
                mod0 = mod0[1:]
            elif not mod0 and not mod2:
                x += str(mod1[0])
                mod1 = mod1[1:]
            elif not mod0 and not mod1:
                x += str(mod2[0])
                mod2 = mod2[1:]
            elif not mod0:
                if mod1[0] > mod2[0]:
                    x += str(mod1[0])
                    mod1 = mod1[1:]
                else:
                    x += str(mod2[0])
                    mod2 = mod2[1:]
            elif not mod1:
                if mod0[0] > mod2[0]:
                    x += str(mod0[0])
                    mod0 = mod0[1:]
                else:
                    x += str(mod2[0])
                    mod2 = mod2[1:]
            elif not mod2:
                if mod1[0] > mod0[0]:
                    x += str(mod1[0])
                    mod1 = mod1[1:]
                else:
                    x += str(mod0[0])
                    mod0 = mod0[1:]
            else:
                if mod1[0] > mod2[0] and mod1[0] > mod0[0]:
                    x += str(mod1[0])
                    mod1 = mod1[1:]
                elif mod0[0] > mod2[0] and mod0[0] > mod1[0]:
                    x += str(mod0[0])
                    mod0 = mod0[1:]
                else:
                    x += str(mod2[0])
                    mod2 = mod2[1:]
        return x