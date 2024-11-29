class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        goodKey = {}
        badKey = {}
        for eq in equations:
            if not eq[0] in goodKey:
                goodKey[eq[0]] = set()
                badKey[eq[0]] = set()
            if not eq[3] in goodKey:
                goodKey[eq[3]] = set()
                badKey[eq[3]] = set()
                
            if eq[1] == "!":
                if eq[3] in goodKey[eq[0]] or eq[0] == eq[3]:
                    return False
                else:
                    badKey[eq[0]].add(eq[3])
                    badKey[eq[3]].add(eq[0])
                    for t in goodKey[eq[3]]:
                        if t in goodKey[eq[0]]:
                            return False
                        if t != eq[0]:
                            badKey[eq[0]].add(t)
                            badKey[t].add(eq[0])
                    for t in goodKey[eq[0]]:
                        if t in goodKey[eq[3]]:
                            return False
                        if t != eq[3]:
                            badKey[eq[3]].add(t)
                            badKey[t].add(eq[3])
            else:
                if eq[3] in badKey[eq[0]]:
                    return False
                else:
                    goodKey[eq[0]].add(eq[3])
                    goodKey[eq[3]].add(eq[0])
                    for t in goodKey[eq[3]]:
                        if t in badKey[eq[0]]:
                            return False
                        if t != eq[0]:
                            goodKey[eq[0]].add(t)
                            goodKey[t].add(eq[0])
                    for t in goodKey[eq[0]]:
                        if t in badKey[eq[3]]:
                            return False
                        if t != eq[3]:
                            goodKey[eq[3]].add(t)
                            goodKey[t].add(eq[3])
                    for t in badKey[eq[3]]:
                        if t in goodKey[eq[0]]:
                            return False
                        if t != eq[0]:
                            badKey[eq[0]].add(t)
                            badKey[t].add(eq[0])
                    for t in badKey[eq[0]]:
                        if t in goodKey[eq[3]]:
                            return False
                        if t != eq[3]:
                            badKey[eq[3]].add(t)
                            badKey[t].add(eq[3])
        return True