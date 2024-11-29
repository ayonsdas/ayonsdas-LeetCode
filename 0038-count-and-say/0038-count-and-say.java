class Solution {
    public String countAndSay(int a) {
        if(a == 1)
            return "1";
        String t = countAndSay(a - 1);
        char c = t.charAt(0);
        int p = 1;
        int n = 1;
        StringBuilder x = new StringBuilder();
        while(p < t.length())
        {
            if(t.charAt(p) == c)
                n += 1;
            else
            {
                x.append(n).append(c);
                c = t.charAt(p);
                n = 1;
            }
            p += 1;
        }
        x.append(n).append(c);
        return x.toString();
    }
}


/**
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        t = self.countAndSay(n - 1)
        c = t[0]
        t = t[1:]
        x = ""
        n = 1
        while t:
            if t[0] == c:
                n += 1
            else:
                x += str(n) + str(c)
                c = t[0]
                n = 1
            t = t[1:]
        x += str(n) + str(c)
        return x

*/