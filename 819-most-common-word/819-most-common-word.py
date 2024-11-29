import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = Counter(re.split("[^A-Za-z]+", paragraph.lower()))
        banned = set([x.lower() for x in banned])
        a = sorted(p.keys(), key = lambda x : -p[x])
        i = 0
        while a[i] in banned or a[i] == "":
            i += 1
        return a[i]