class Solution {
public:
    string removeDuplicates(string s) {
        string r = "";
        for(char a : s)
            if(r.size() > 0 && r.back() == a)
                r.pop_back();
            else
                r.push_back(a);
        return r;
    }
};