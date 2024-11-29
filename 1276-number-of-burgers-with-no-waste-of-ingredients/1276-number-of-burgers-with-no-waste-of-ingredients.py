class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0 or tomatoSlices < 2 * cheeseSlices or tomatoSlices > 4 * cheeseSlices:
            return []
        x = tomatoSlices // 2 - cheeseSlices
        return [x, cheeseSlices - x]