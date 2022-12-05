class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low & 1 ^ high & 1:
            return (high - low) // 2 + 1
        if low & 1:
            return (high - low) // 2 + 1
        return (high - low) // 2