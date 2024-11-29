class Solution:
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        digits = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        stuff = ["Thousand", "Million", "Billion", "Trillion"]
        
        i = 0
        finalString = []
        while num > 0:
            x = str(num % 1000)
            num = num // 1000
            string = []
            if len(x) == 3:
                string.append(digits[int(x[0])])
                string.append("Hundred")
                x = x[1:]
            if len(x) == 2:
                if x[0] == '0':
                    x = x[1:]
                elif x[0] == '1':
                    string.append(teens[int(x) - 10])
                    x = x[2:]
                else:
                    string.append(tens[int(x[0]) - 2])
                    x = x[1:]
            if len(x) == 1 and x != '0':
                string.append(digits[int(x)])
            if i != 0 and len(string) > 0:
                string.append(stuff[i - 1])
            i += 1
            if len(string) > 0:
                finalString.insert(0, " ".join(string))
        return " ".join(finalString)