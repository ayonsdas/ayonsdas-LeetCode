class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        c = 0
        r = []
        a = []
        while words:
            if c + len(words[0]) + len(a) > maxWidth:
                if len(a) > 1:
                    x = ""
                    spaces = maxWidth - c
                    more, least = spaces % (len(a) - 1), spaces // (len(a) - 1)
                    for i in range(len(a) - 1):
                        x += a[i]
                        if i < more:
                            x += " "
                        for j in range(least):
                            x += " "
                    x += a[-1]
                    r.append(x)
                else:
                    a = a[0]
                    while len(a) < maxWidth:
                        a += " "
                    r.append(a)
                a = [words[0]]
                c = len(words[0])
            else:
                c += len(words[0])
                a.append(words[0])
            words = words[1:]
        if a:
            a = " ".join(a)
            while len(a) < maxWidth:
                a += " "
            r.append(a)
        return r