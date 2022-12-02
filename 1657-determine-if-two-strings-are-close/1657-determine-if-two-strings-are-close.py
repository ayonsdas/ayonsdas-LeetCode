class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1, word2 = Counter(word1), Counter(word2)
        if word1.keys() != word2.keys():
            return False
        word1, word2 = Counter([word1[a] for a in word1]), Counter([word2[a] for a in word2])
        return word1 == word2