class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        r = Counter(words)
        l = list(r.keys())
        l.sort()
        l = sorted(l, key = lambda x: -r[x])
        return l[:k]