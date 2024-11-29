class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        def finder(x: int, y: int) -> bool:
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == ".":
                return False
            board[x][y] = "."
            finder(x + 1, y)
            finder(x, y + 1)
            finder(x - 1, y)
            finder(x, y - 1)
            return True
        c = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if finder(i, j):
                    c += 1
        
        return c