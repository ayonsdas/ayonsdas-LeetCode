class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        c = 0
        v = 0
        for x in transactions:
            c += max(0, x[0] - x[1])
            v = max(v, min(x[0], x[1]))
        return c + v