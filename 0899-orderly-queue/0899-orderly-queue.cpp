class Solution {
public:
    string orderlyQueue(string s, int k) {
        if(k == 0)
            return s;
        if(k > 1)
        {
            sort(s.begin(), s.end());
            return s;
        }
        string st = s;
        for(int i = 1; i < s.size(); i++)
        {
            string p = s.substr(i) + s.substr(0, i);
            if(st > p)
                st = p;
        }
        return st;
    }
}; 