class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if not endWord in wordList:
            return 0
        q = collections.deque([[beginWord, 1]])
        while q:
            t = q.popleft()
            if t[0] == endWord:
                return t[1]
            for i in range(len(t[0])):
                for j in range(26):
                    new = t[0][:i] + chr(j + 97) + t[0][i + 1:]
                    if new in wordList:
                        wordList.remove(new)
                        q.append([new, t[1] + 1])
        return 0