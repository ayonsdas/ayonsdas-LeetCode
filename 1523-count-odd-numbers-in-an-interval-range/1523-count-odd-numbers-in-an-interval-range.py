class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low & 1 or high & 1:
            return (high - low) // 2 + 1
        return (high - low) // 2