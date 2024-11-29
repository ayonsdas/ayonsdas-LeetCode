class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        table = [float('inf') for _ in range(amount + 1)]
        table[0] = 0
        for i in range(amount):
            for j in range(len(coins)):
                if i + coins[j] <= amount:
                    table[i + coins[j]] = min(table[i + coins[j]], table[i] + 1)
        return table[-1] if table[-1] != float('inf') else -1