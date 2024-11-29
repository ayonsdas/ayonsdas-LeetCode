class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        wordDict = Counter(word)
        boardDict = defaultdict(int)
        for a in board:
            for x in a:
                boardDict[x] += 1
        for l in wordDict:
            if not l in boardDict or boardDict[l] < wordDict[l]:
                return False
        
        def finder(x: int, y: int, c: int) -> bool:
            nonlocal board, word
            if c == len(word):
                return True
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != word[c]:
                return False
            a = board[x][y]
            board[x][y] = "-"
            u, l, r, d = finder(x - 1, y, c + 1), finder(x, y - 1, c + 1), finder(x, y + 1, c + 1), finder(x + 1, y, c + 1)
            board[x][y] = a
            return u or l or r or d
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if finder(i, j, 0):
                    return True
        return False