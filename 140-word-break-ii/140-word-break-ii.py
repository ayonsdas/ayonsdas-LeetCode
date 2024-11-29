class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.finder(s, wordDict, [])
    
    def finder(self, s: str, wordDict: List[str], currWords: List[str]) -> List[str]:
        if s == "":
            return [" ".join(currWords)]
        x = []
        for word in wordDict:
            if len(s) >= len(word) and s[0:len(word)] == word:
                l = [t for t in currWords]
                l.append(word)
                for b in self.finder(s[len(word):], wordDict, l):
                    x.append(b)
        return x