public class Solution {
    public int MinMutation(string start, string end, string[] bank) {
        Dictionary<string, HashSet<string>> m = new Dictionary<string, HashSet<string>>();
        Queue<string> q = new Queue<string>();
        m[start] = new HashSet<string>();
        foreach(string a in bank)
        {
            if(!(m.ContainsKey(a)))
                m[a] = new HashSet<string>();
            
            if(oneOff(start, a))
            {
                m[start].Add(a);
                m[a].Add(start);
            }
            foreach(string b in bank)
            {
                if(!(m.ContainsKey(b)))
                    m[b] = new HashSet<string>();
                
                if(oneOff(a, b))
                {
                    m[b].Add(a);
                    m[a].Add(b);
                }
            }
        }
        
        HashSet<string> v = new HashSet<string>();
        
        int r = 0;
        
        q.Enqueue(start);
        while(q.Count() != 0)
        {
            int sz = q.Count();
            for(int i = 0; i < sz; i++)
            {
                string a = q.Dequeue();
                
                if(a == end)
                    return r;
                
                v.Add(a);
                
                foreach(string x in m[a])
                    if(!v.Contains(x))
                        q.Enqueue(x);
            }
            r++;
        }
        return -1;
    }
    
    private bool oneOff(string a, string b)
    {
        bool x = false;
        for(int i = 0; i < 8; i++)
        {
            if(a[i] != b[i])
                if(x)
                    return false;
                else
                    x = true;
        }
        return x;
    }
}