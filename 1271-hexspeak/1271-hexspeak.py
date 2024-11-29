class Solution:
    def toHexspeak(self, num: str) -> str:
        num = [char for char in hex(int(num))[2:].upper()]
        for i in range(len(num)):
            if ord(num[i]) < 65 or ord(num[i]) > 70:
                if num[i] == "0":
                    num[i] = "O"
                elif num[i] == "1":
                    num[i] = "I"
                else:
                    return "ERROR"
        return "".join(num)