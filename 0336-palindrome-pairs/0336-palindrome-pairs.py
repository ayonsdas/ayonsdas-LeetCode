class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        m = {}
        for i, word in enumerate(words):
            m[word] = i
            
        a = set()
        for i, word in enumerate(words):
            if not word:
                continue

            for j in range(len(word)):
                current = word[:j]
                target = word[j:][::-1]
                if current == current[::-1] and target != word and target in m:
                    a.add((m[target], i))
                    
            for j in range(len(word), -1, -1):
                current = word[j:]
                target = word[:j][::-1]
                if current == current[::-1] and target != word and target in m:
                    a.add((i, m[target]))
                    
            if word == word[::-1] and "" in m:
                idx = m[""]
                a.add((i, idx))
                a.add((idx, i))

        return list(a)