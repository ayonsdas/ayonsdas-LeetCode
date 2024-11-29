class Solution:
    def isHappy(self, n: int) -> bool:
        
        s = set()
        while True:
            if n == 1:
                return True
            if n in s:
                return False
            s.add(n)
            n = self.modify(n)
        
        return s == 1
            
    def modify(self, n: int) -> int:
        t = 0
        while n:
            t += (n % 10) ** 2
            n //= 10
        return t