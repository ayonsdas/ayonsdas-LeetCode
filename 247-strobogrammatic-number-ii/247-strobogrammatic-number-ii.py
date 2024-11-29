class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        return self.finder(n, False)
    
    def finder(self, n: int, b: bool) -> List[str]:
        if n == 1:
            return ["0", "1", "8"]
        if n == 2:
            if b:
                return ["00", "11", "69", "88", "96"]
            else:
                return ["11", "69", "88", "96"]
        t = ["11", "69", "88", "96"]
        if b:
            t.append("00")
        j = self.finder(n - 2, True)
        s = []
        for x in j:
            for y in t:
                s.append(y[0] + x + y[1])
        return s