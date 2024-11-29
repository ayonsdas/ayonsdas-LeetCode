class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def valRow(x: int) -> bool:
            nonlocal board
            aSet = set()
            for j in range(9):
                if board[x][j] != ".":
                    if board[x][j] in aSet:
                        return False
                    aSet.add(board[x][j])
            return True
        
        def valCol(y: int) -> bool:
            nonlocal board
            aSet = set()
            for i in range(9):
                if board[i][y] != ".":
                    if board[i][y] in aSet:
                        return False
                    aSet.add(board[i][y])
            return True
        
        def valSquare(x: int, y: int) -> bool:
            nonlocal board
            aSet = set()
            x //= 3
            y //= 3
            x *= 3
            y *= 3
            for i in range(3):
                for j in range(3):
                    if board[x + i][y + j] != ".":
                        if board[x + i][y + j] in aSet:
                            return False
                        aSet.add(board[x + i][y + j])
            return True
        
        def validCheck(x: int, y: int) -> bool:
            return valRow(x) and valCol(y) and valSquare(x, y)
        
        def checkTrue(p: int) -> bool:
            nonlocal board
            if p == 81:
                return True
            x, y = p // 9, p % 9
            if board[x][y] != ".":
                return checkTrue(p + 1)
            for i in range(1, 10):
                board[x][y] = str(i)
                if validCheck(x, y):
                    if checkTrue(p + 1):
                        return True
            board[x][y] = "."
            return False
                
        
            
        checkTrue(0)