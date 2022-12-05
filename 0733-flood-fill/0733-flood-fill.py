class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        def ffHelper(r, c, prev):
            nonlocal image, color
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != prev:
                return
            image[r][c] = color
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ffHelper(r + x, c + y, prev)
            
            
        ffHelper(sr, sc, image[sr][sc])
        return image