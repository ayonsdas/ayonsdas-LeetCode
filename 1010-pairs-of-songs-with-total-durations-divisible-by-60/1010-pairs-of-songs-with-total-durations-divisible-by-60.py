class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        keys = {}
        for t in time:
            if not t % 60 in keys:
                keys[t % 60] = 0
            keys[t % 60] += 1
        c = 0
        for key in keys:
            if key != 0 and key != 30:
                if 60 - key in keys:
                    c += keys[key] * keys[60 - key]
        
        c //= 2
        if 0 in keys:
            c += keys[0] * (keys[0] - 1) // 2
        if 30 in keys:
            c += keys[30] * (keys[30] - 1) // 2
            
        return c