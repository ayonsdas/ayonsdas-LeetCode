class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        L = [len(dominoes) for x in dominoes]
        R = [len(dominoes) for x in dominoes]
        c = 0
        adding = False
        for i in range(len(dominoes)):
            if dominoes[i] == ".":
                if adding:
                    R[i] = c
                    c += 1
            else:
                if dominoes[i] == "R":
                    adding = True
                    R[i] = 0
                    c = 1
                else:
                    adding = False
                    c = 0
        adding = False
        c = 0
        for i in range(len(dominoes)):
            if dominoes[~i] == ".":
                if adding:
                    L[~i] = c
                    c += 1
            else:
                if dominoes[~i] == "L":
                    adding = True
                    L[~i] = 0
                    c = 1
                else:
                    adding = False
                    c = 0
        x = ""
        for i in range(len(dominoes)):
            if L[i] < R[i]:
                x += "L"
            elif L[i] > R[i]:
                x += "R"
            else:
                x += "."
        return x