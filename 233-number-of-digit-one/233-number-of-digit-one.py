class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        x = [0] * (math.floor(math.log10(n)) + 1)
        for i in range(len(x)):
            j = int(str(n)[0:~i] if i != len(x) - 1 else '0')
            k = int(str(n)[-i:] if i != 0 else '0')
            x[~i] = j * 10 ** i
            if int(str(n)[~i]) == 1:
                x[~i] += k + 1
            elif int(str(n)[~i]) > 1:
                x[~i] += 10 ** i
        return sum(x)