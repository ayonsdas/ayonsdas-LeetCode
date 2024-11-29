class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        t = [1]
        for i in range(rowIndex):
            l = [1]
            for i in range(1, len(t)):
                l.append(t[i - 1] + t[i])
            l.append(1)
            t = l
        return t