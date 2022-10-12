class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        l = ""
        for i in range(n):
            l += "0"
        t = [l]
        s = set()
        s.add(l)
        
        def finder() -> bool:
            nonlocal t, n, s
            if len(t) == 2 ** n:
                b = t[-1]
                c = 0
                for ls in b:
                    if ls == "1":
                        c += 1
                return c == 1
            x = []
            for i in range(n):
                r = [char for char in t[-1]]
                if r[i] == "0":
                    r[i] = "1"
                else:
                    r[i] = "0"
                r = "".join(r)
                if not r in s:
                    x.append(r)
            for a in x:
                t.append(a)
                s.add(a)
                if finder():
                    return True
                t.pop(-1)
                s.remove(a)
            return False
            
        finder()
        return [int(x, 2) for x in t]