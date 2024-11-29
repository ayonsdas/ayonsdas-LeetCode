class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                x = board[3 * i : 3 * i + 3]
                for m in range(3):
                    x[m] = x[m][3 * j : 3 * j + 3]
                found = [False] * 10
                for t in x:
                    for l in t:
                        if l != '.':
                            if found[int(l)]:
                                return False
                            found[int(l)] = True
        for i in range(9):
            x = board[i]
            found = [False] * 10
            for l in x:
                if l != '.':
                    if found[int(l)]:
                        return False
                    found[int(l)] = True
                
        for j in range(9):
            x = []
            for i in range(9):
                x.append(board[i][j])
            found = [False] * 10
            for l in x:
                if l != '.':
                    if found[int(l)]:
                        return False
                    found[int(l)] = True
        return True