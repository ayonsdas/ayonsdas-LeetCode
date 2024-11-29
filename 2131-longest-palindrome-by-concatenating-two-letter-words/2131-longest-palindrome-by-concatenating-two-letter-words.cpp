class Solution {
public:
    int longestPalindrome(vector<string>& words)
    {
        unordered_map<string, int> m;
        int c = 0;
        int d = 0;
        for(string word : words)
        {
            m[word] += 1;
        }
        for(auto word : m)
        {
            if(word.first[0] == word.first[1])
            {
                d += 4 * (word.second / 2);
                if(word.second % 2 == 1)
                    c = 2;
            }
            else if (m.count(word.first.substr(1) + word.first.substr(0, 1)))
                d += 2 * min(m[word.first], m[word.first.substr(1) + word.first.substr(0, 1)]);
        }
        return c + d;
    }
};