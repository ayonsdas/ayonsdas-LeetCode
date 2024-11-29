class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        s = {}
        for i in range(26):
            a, b = i // 5, i % 5
            s[chr(i + 97)] = [a, b]
        r = ""
        for i in range(len(target)):
            x, y = s[target[i]][0] - (s[target[i - 1]][0] if i > 0 else 0), s[target[i]][1] - (s[target[i - 1]][1] if i > 0 else 0)
            if i > 0 and s[target[i - 1]][0] == 5:
                for i in range(-x):
                    r += "U"
                for i in range(y):
                    r += "R"
                r += "!"
            else:
                if y > 0:
                    for i in range(y):
                        r += "R"
                else:
                    for i in range(-y):
                        r += "L"
                if x > 0:
                    for i in range(x):
                        r += "D"
                else:
                    for i in range(-x):
                        r += "U"
                r += "!"
        return r