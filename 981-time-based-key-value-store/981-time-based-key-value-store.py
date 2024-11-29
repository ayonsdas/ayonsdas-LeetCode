class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.keys:
            self.keys[key] = [["", value], [0, timestamp]]
        else:
            self.keys[key][0].append(value)
            self.keys[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.keys:
            return ""
        a = self.keys[key]
        l = 0
        r = len(a[1]) - 1
        while r - l > 1:
            m = (l + r) // 2
            if a[1][m] > timestamp:
                r = m - 1
            elif a[1][m] < timestamp:
                l = m + 1
            else:
                return a[0][m]
        if r == l:
            if a[1][r] > timestamp:
                return a[0][r - 1]
            return a[0][r]
        else:
            if a[1][r] > timestamp:
                if a[1][l] <= timestamp:
                    return a[0][l]
                else:
                    return a[0][l - 1]
            else:
                return a[0][r]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)