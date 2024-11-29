class Solution:
    def differByOne(self, dicti: List[str]) -> bool:
        for i in range(len(dicti[0])):
            t = set()
            for word in dicti:
                x = word[0:i] + "-" + word[i + 1:]
                if x in t:
                    return True
                t.add(x)
        return False