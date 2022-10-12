class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        s = []
        def f(t: List[int], a: int):
            if len(t) == k:
                s.append(t)
                return
            if a > n:
                return
            b, c = [x for x in t], [x for x in t]
            c.append(a)
            f(b, a + 1)
            f(c, a + 1)
        f([], 1)
            
        return s