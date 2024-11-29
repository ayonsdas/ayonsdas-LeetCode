class Solution:
    def checkRecord(self, st: str) -> bool:
        a = 0
        l = 0
        for s in st:
            if s == "L":
                l += 1
                if l == 3:
                    return False
            else:
                l = 0
                if s == 'A':
                    a += 1
                    if a == 2:
                        return False
        return True