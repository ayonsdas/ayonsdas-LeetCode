class Solution:
    def isNumber(self, s: str) -> bool:
        key = s.lower().split("e")
        if len(key) > 2:
            return False
        val = key[0]
        if len(val) == 0:
            return False
        if val[0] == '+' or val[0] == '-':
            val = val[1:]
        if len(val) == 0:
            return False
        numFound = False
        dotFound = False
        for i in val:
            if ord(i) < 48 or ord(i) > 57:
                if not dotFound and i == '.':
                    dotFound = True
                else:
                    return False
            else:
                numFound = True
        if not numFound:
            return False
        if len(key) == 2:
            val = key[1]
            if len(val) == 0:
                return False
            if val[0] == '+' or val[0] == '-':
                val = val[1:]
            if len(val) == 0:
                return False
            for i in val:
                if ord(i) < 48 or ord(i) > 57:
                    return False
        return True