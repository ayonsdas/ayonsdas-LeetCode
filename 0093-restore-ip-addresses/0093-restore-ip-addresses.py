class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        sol = []
        self.finder([], s, sol)
        return sol
    
    def finder(self, curr: List[str], s: str, sol: List[str]) -> None:
        
        if not s:
            if len(curr) == 4:
                sol.append(".".join(curr))
            return
        if s == "0":
            curr.append(s[0])
            self.finder(curr, s[1:], sol)
            curr.pop(-1)
            return
        curr.append(s[0])
        self.finder(curr, s[1:], sol)
        curr.pop(-1)
        if s[0] == "0" or len(s) == 1:
            return
        curr.append(s[:2])
        self.finder(curr, s[2:], sol)
        curr.pop(-1)
        if len(s) >= 3 and int(s[:3]) <= 255:
            curr.append(s[:3])
            self.finder(curr, s[3:], sol)
            curr.pop(-1) 