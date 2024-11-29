# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        i = 0
        j = binaryMatrix.dimensions()[1] - 1
        while i < binaryMatrix.dimensions()[0] and j >= 0:
            if binaryMatrix.get(i, j) == 0:
                i += 1
            else:
                j -= 1
        return j + 1 if j != binaryMatrix.dimensions()[1] - 1else -1