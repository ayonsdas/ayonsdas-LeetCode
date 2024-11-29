class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        a, b, c = set(), set(), set()
        for match in matches:
            if not(match[0] in a or match[0] in b or match[0] in c):
                a.add(match[0])
            if match[1] in a:
                a.remove(match[1])
                b.add(match[1])
            elif match[1] in b:
                b.remove(match[1])
                c.add(match[1])
            elif match[1] not in c:
                b.add(match[1])
        return [sorted(list(a)), sorted(list(b))]