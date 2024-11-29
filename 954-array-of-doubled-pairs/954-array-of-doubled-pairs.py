class Solution:
    def canReorderDoubled(self, changed: List[int]) -> List[int]:
        stuff = Counter(changed)
        x = sorted(stuff.keys(), key = lambda x : abs(x))
        i = 0
        while i < len(x):
            if x[i] == 0:
                if stuff[0] > 1:
                    stuff[0] -= 2
                elif stuff[0] == 0:
                    i += 1
                else:
                    return False
            else:
                if stuff[x[i]] > 0:
                    if x[i] * 2 in stuff and stuff[x[i] * 2] > 0:
                        stuff[x[i]] -= 1
                        stuff[x[i] * 2] -= 1
                    else:
                        return False
                else:
                    i += 1
        return True