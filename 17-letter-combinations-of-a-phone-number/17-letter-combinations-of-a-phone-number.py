class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = [[] for i in range(8)]
        i = 0
        while i < 26:
            t = chr(i + 97)
            if i < 3:
                d[0].append(t)
            elif i < 6:
                d[1].append(t)
            elif i < 9:
                d[2].append(t)
            elif i < 12:
                d[3].append(t)
            elif i < 15:
                d[4].append(t)
            elif i < 19:
                d[5].append(t)
            elif i < 22:
                d[6].append(t)
            else:
                d[7].append(t)
            i += 1
        t = self.letterCombinations(digits[1:])
        if not t:
            t.append("")
        x = []
        for a in d[int(digits[0]) - 2]:
            for b in t:
                x.append(a + b)
        return x