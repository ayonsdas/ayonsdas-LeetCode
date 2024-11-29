class Solution:
    def merge(self, v: List[List[int]]) -> List[List[int]]:
        v = sorted(v, key = lambda x : x[0])
        i = 1
        l, r = v[0][0], v[0][1]
        t = []
        while i < len(v):
            if v[i][0] > r:
                t.append([l, r])
                l, r = v[i][0], v[i][1]
            else:
                r = max(r, v[i][1])
            i += 1
        t.append([l, r])
        return t