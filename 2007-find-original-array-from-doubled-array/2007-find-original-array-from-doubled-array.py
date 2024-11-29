class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        stuff = {}
        for i in range(len(changed)):
            if not changed[i] in stuff:
                stuff[changed[i]] = 0
            stuff[changed[i]] += 1
        bruh = []
        x = sorted(stuff.keys())
        i = 0
        while i < len(x):
            if x[i] == 0:
                if stuff[0] > 1:
                    bruh.append(0)
                    stuff[0] -= 2
                elif stuff[0] == 0:
                    i += 1
                else:
                    return []
            else:
                if stuff[x[i]] > 0:
                    if x[i] * 2 in stuff and stuff[x[i] * 2] > 0:
                        bruh.append(x[i])
                        stuff[x[i]] -= 1
                        stuff[x[i] * 2] -= 1
                    else:
                        return []
                else:
                    i += 1
        return bruh