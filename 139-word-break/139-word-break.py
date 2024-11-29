class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        found = [False for _ in range(len(s) + 1)]
        found[0] = True
        
        for i in range(len(s)):
            if not found[i]:
                continue
            
            for k in range(min(20, len(s) - i), 0, -1):
                if s[i:i+k] in wordDict:
                    found[i + k] = True
            
        return found[-1]