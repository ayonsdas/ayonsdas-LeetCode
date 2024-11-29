class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        t = set()
        r = set()
        for i in range(len(s) - 9):
            x = s[i:i+10]
            if x in t:
                r.add(x)
            else:
                t.add(x)
        return list(r)