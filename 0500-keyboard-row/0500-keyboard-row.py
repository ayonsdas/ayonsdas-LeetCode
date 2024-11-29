class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = set([char for char in "qwertyuiop"])
        b = set([char for char in "asdfghjkl"])
        c = set([char for char in "zxcvbnm"])
        x = []
        for word in words:
            l = -1
            for char in word:
                if char in a:
                    if l == -1 or l == 1:
                        l = 1
                    else:
                        break
                if char in b:
                    if l == -1 or l == 2:
                        l = 2
                    else:
                        break
                if char in c:
                    if l == -1 or l == 3:
                        l = 3
                    else:
                        break
            else:
                x.append(word)
        return x