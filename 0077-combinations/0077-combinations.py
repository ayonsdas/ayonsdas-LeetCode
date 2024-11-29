class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        s = []
        def f(t: List[int], a: int):
            if len(t) == k:
                s.append(t)
                return
            if a > n:
                return
            f([x for x in t], a + 1)
            t.append(a)
            f([x for x in t], a + 1)
        f([], 1)
            
        return s