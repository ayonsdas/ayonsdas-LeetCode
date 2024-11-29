class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 - x[~i] for i in range(len(x))] for x in image]