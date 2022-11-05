class Solution {
public:
    bool exist(vector<vector<char>>& board, string word)
    {
        unordered_map<char, int> m;
        for(char c : word)
            m[c]++;
        
        unordered_map<char, int> m2;
        for(vector<char>& bo : board)
            for(char c : bo)
                m2[c]++;
        
        for(auto pair : m)
            if(m[pair.first] > m2[pair.first])
                return false;
        
        for(int i = 0; i < board.size(); i++)
            for(int j = 0; j < board[i].size(); j++)
                if(dfs(board, i, j, word, 0))
                    return true;
        return false;
    }
    
    bool dfs(vector<vector<char>>& board, int x, int y, string word, int p)
    {
        if(p == word.size())
            return true;
        
        if(x < 0 || y < 0 || x >= board.size() || y >= board[0].size() || board[x][y] != word[p])
            return false;
        
        char c = board[x][y];
        board[x][y] = '#';
        
        if(dfs(board, x - 1, y, word, p + 1))
            return true;
        
        if(dfs(board, x + 1, y, word, p + 1))
            return true;
        
        if(dfs(board, x, y - 1, word, p + 1))
            return true;
        
        if(dfs(board, x, y + 1, word, p + 1))
            return true;
        
        board[x][y] = c;
        
        return false;
    }
};