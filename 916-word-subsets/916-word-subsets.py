class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        m = []
        t = defaultdict(int)
        for word2 in words2:
            k = Counter(word2)
            for char in k:
                t[char] = max(t[char], k[char])
        for word in words1:
            k = Counter(word)
            for char in t:
                if not char in k or k[char] < t[char]:
                    break
            else:
                m.append(word)
        return m