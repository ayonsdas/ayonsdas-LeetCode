class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    c = 0
                    x, y = i, j
                    while board[x][y] != "p":
                        x -= 1
                        if x < 0 or board[x][y] == "B":
                            break
                    else:
                        c += 1
                        
                    x, y = i, j
                    while board[x][y] != "p":
                        y -= 1
                        if y < 0 or board[x][y] == "B":
                            break
                    else:
                        c += 1
                        
                    x, y = i, j
                    while board[x][y] != "p":
                        x += 1
                        if x >= len(board) or board[x][y] == "B":
                            break
                    else:
                        c += 1
                        
                    x, y = i, j
                    while board[x][y] != "p":
                        y += 1
                        if y >= len(board[0]) or board[x][y] == "B":
                            break
                    else:
                        c += 1
                    
                    return c