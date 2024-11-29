class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        key = {}
        for i in range(len(manager)):
            if not manager[i] in key:
                key[manager[i]] = [0, []]
            key[manager[i]][1].append(i)
            if not i in key:
                key[i] = [0, []]
            key[i][0] = informTime[i]
        
        q = [key[-1][1][0]]
        s = 0
        while q:
            l = q.pop(-1)
            s = max(s, key[l][0])
            for a in key[l][1]:
                key[a][0] += key[l][0]
                q.append(a)
        return s