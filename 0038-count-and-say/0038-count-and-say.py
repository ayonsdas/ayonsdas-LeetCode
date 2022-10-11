class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        t = self.countAndSay(n - 1)
        c = t[0]
        t = t[1:]
        x = []
        n = 1
        while t:
            if t[0] == c:
                n += 1
            else:
                x.append([n, c])
                c = t[0]
                n = 1
            t = t[1:]
        x.append([n, c])
        return "".join([str(a[0]) + str(a[1]) for a in x])
        print(x)