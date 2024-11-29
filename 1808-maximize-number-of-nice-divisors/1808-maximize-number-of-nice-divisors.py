class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors < 3:
            return primeFactors
        if primeFactors % 3 == 0:
            return pow(3, primeFactors // 3, 10 ** 9 + 7)
        elif primeFactors % 3 == 1:
            return pow(3, primeFactors // 3 - 1, 10 ** 9 + 7) * 4 % (10 ** 9 + 7)
        return pow(3, primeFactors // 3, 10 ** 9 + 7) * 2 % (10 ** 9 + 7)