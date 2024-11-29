#include <unordered_set>

class Solution {
public:
    string reverseVowels(string s) {
        int i = 0;
        unordered_set<char> st {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int j = s.size() - 1;
        while(true)
        {
            if(i >= j)
                break;
            while(i < s.size() && !st.count(s[i]))
                i++;
            if(i >= j)
                break;
            while(j >= 0 && !st.count(s[j]))
                j--;
            if(i >= j)
                break;
            char temp = s[j];
            s[j--] = s[i];
            s[i++] = temp;
        }
        return s;
    }
};