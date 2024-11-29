class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        x = []
        for j in range(2, n + 1):
            for i in range(1, j):
                if math.gcd(i, j) == 1 or i == 1:
                    x.append(str(i) + "/" + str(j))
        return x