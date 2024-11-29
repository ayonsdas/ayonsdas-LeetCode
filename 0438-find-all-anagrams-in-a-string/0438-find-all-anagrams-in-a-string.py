class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a = Counter(p)
        b = Counter(s[0:len(p)])
        r = []
        for i in range(len(s) - len(p)):
            if a == b:
                r.append(i)
            if not s[i + len(p)] in b:
                b[s[i + len(p)]] = 0
            b[s[i + len(p)]] += 1
            b[s[i]] -= 1
        if a == b:
            r.append(len(s) - len(p))
        return r