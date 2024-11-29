class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        d = set(arr2)
        x = []
        for l in arr2:
            for i in range(c[l]):
                x.append(l)
        for g in sorted(c.keys()):
            if not g in d:
                for i in range(c[g]):
                    x.append(g)
        return x


