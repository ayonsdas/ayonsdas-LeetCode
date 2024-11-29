class Solution:
    def thousandSeparator(self, n: int) -> str:
        t = ""
        n = str(n)
        for i in range(len(n)):
            if i % 3 == 0 and i != 0:
                t += "."
            t += n[~i]
        return t[::-1]