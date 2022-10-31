#include <queue>
#include <map>
#include <unordered_set>
#include <string>

class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        
        map<string, unordered_set<string>> m;
        queue<string> q;
        int s = 0;
        m[start] = unordered_set<string>();
        for(string a : bank)
        {
            m[a] = unordered_set<string>();
            if(oneOff(a, start))
            {
                m[start].insert(a);
                m[a].insert(start);
            }
            for(string b: bank)
            {
                if(oneOff(a, b))
                {
                    m[b].insert(a);
                    m[a].insert(b);
                }
            }
        }
        q.push(start);
        int r = 0;
        unordered_set<string> v;
        while(!q.empty())
        {
            int sz = q.size();
            for(int i = 0; i < sz; i++)
            {
                string n = q.front();
                q.pop();
                
                if(n == end)
                    return r;
                    
                for(string a : m[n])
                    if(!v.count(a))
                        q.push(a);
                
                v.insert(n);
            }
            r++;
        }
        return -1;
    }
    
    bool oneOff(string a, string b) {
        bool x = false;
        for(int i = 0; i < 8; i++)
        {
            if(a[i] != b[i])
            {
                if(x)
                    return false;
                x = true;
            }
        }
        return x;
    }
};