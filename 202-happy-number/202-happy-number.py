class Solution:
    def isHappy(self, n: int) -> bool:
        
        s = f = n
        while True:
            s = self.modify(s)
            f = self.modify(self.modify(f))
            if s == f:
                break
        
        return s == 1
            
    def modify(self, n: int) -> int:
        t = 0
        while n:
            t += (n % 10) ** 2
            n //= 10
        return t