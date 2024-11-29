class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        
        if num % 10 == 4:
            s += "VI"
            num -= 4
        elif num % 10 == 9:
            s += "XI"
            num -= 9
        while num % 10 != 0 and num % 10 != 5:
            s += "I"
            num -= 1
        if num % 10 == 5:
            s += "V"
            num -= 5
        
        if num % 100 == 40:
            s += "LX"
            num -= 40
        elif num % 100 == 90:
            s += "CX"
            num -= 90
        while num % 100 != 0 and num % 100 != 50:
            s += "X"
            num -= 10
        if num % 100 == 50:
            s += "L"
            num -= 50
        
        if num % 1000 == 400:
            s += "DC"
            num -= 400
        elif num % 1000 == 900:
            s += "MC"
            num -= 900
        while num % 1000 != 0 and num % 1000 != 500:
            s += "C"
            num -= 100
        if num % 1000 == 500:
            s += "D"
            num -= 500
            
        while num != 0:
            s += "M"
            num -= 1000
            
        return s[::-1]