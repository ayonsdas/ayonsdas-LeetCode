class Solution {
    fun isPalindrome(s: String): Boolean {
        var i = 0;
        var j = s.length - 1;
        while(i < j)
        {
            while(i < s.length && (s[i] < 'A' || s[i] > 'Z') && (s[i] < 'a' || s[i] > 'z') && (s[i] < '0' || s[i] > '9'))
                i++;
            
            while(j >= 0 && (s[j] < 'A' || s[j] > 'Z') && (s[j] < 'a' || s[j] > 'z') && (s[j] < '0' || s[j] > '9'))
                j--;
            
            if(i >= s.length && j < 0)
                return true;
            
            if(i >= s.length || j < 0)
                return false;
            
            if(s[i].toLowerCase() != s[j].toLowerCase())
                return false;
            
            i++;
            j--;
        }
        return true;
    }
}


/**

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:

            print(ord(s[j]))
            while i < len(s) and (ord(s[i]) < 65 or ord(s[i]) > 90) and (ord(s[i]) < 97 or ord(s[i]) > 122) and (ord(s[i]) < 48 or ord(s[i]) > 57):
                i += 1
            while j >= 0 and (ord(s[j]) < 65 or ord(s[j]) > 90) and (ord(s[j]) < 97 or ord(s[j]) > 122) and (ord(s[j]) < 48 or ord(s[j]) > 57):
                j -= 1

            if i >= len(s) and j < 0:
                return True
            if i >= len(s) or j < 0:
                return False
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        
*/