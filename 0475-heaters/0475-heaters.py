class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        
        memo_heater = set(heaters)
        
        res = 0
        
        for house in houses:
            if house not in memo_heater:
                index = bisect.bisect(heaters, house)
                
                # three kind of senario:
                # 1. target: 0 arrary:[2, 5]
                #   -> get: 0
                # 2. target: 3 arrary:[2, 5]
                #   -> get: 1
                # 3. target: 7 arrary:[2, 5]
                #   -> get: 2
                # 4. target: 2 arrary:[2, 5]
                #   -> get: 0
                # 5. target: 5 arrary:[2, 5]
                #   -> get: 2
                
                if index == 0:
                    res = max(res, heaters[index] - house)
                elif index >= len(heaters):
                    res = max(res, house - heaters[len(heaters) - 1])
                else:
                    left = house - heaters[index - 1]
                    right = heaters[index] - house
                    short = min(left, right)
                    res = max(res, short)
                    
        return res