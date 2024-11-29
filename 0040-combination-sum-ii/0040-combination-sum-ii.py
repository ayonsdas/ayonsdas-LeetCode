class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        while candidates and candidates[-1] > target:
            candidates.pop(-1)
        candidates = Counter(candidates)
        l = list(candidates.keys())
        s = []
        def solver(available: List[int], used: List[int], soFar: int) -> None:
            nonlocal target, s
            if soFar == target:
                s.append([x for x in used])
                return
            if not available:
                return
            for i in range(candidates[available[0]] + 1):
                if soFar + i * available[0] <= target:
                    t = [a for a in used]
                    for k in range(i):
                        t.append(available[0])
                    solver(available[1:], t, soFar + i * available[0])
                else:
                    break
        solver(l, [], 0)
        return s