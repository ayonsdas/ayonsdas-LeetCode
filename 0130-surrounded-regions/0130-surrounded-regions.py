class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        
        def marker(x: int, y: int) -> bool:
            nonlocal board, visited
            if board[x][y] != "O" or (x, y) in visited:
                return False
            visited.add((x, y))
            if x == 0 or x == len(board) - 1 or y == 0 or y == len(board[0]) - 1:
                return board[x][y] == "O"
            u, l, r, d = marker(x - 1, y), marker(x, y - 1), marker(x, y + 1), marker(x + 1, y)
            return u or l or r or d
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    visited = set()
                    if not marker(i, j):
                        for a, b in visited:
                            board[a][b] = "X"