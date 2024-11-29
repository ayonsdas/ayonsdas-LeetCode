class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        setA = set([chr(a + 97) for a in range(26)])
        for s in sentence:
            if s in setA:
                setA.remove(s)
        return not setA