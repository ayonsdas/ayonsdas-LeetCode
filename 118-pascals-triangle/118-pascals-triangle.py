class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        b = [[1]]
        while len(b) < numRows:
            x = [1]
            for t in range(1, len(b)):
                x.append(b[-1][t - 1] + b[-1][t])
            x.append(1)
            b.append(x)
        return b