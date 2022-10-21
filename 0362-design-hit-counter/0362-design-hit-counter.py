class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        l = 0
        r = len(self.hits) - 1
        v2 = -1
        while l <= r:
            m = (l + r) // 2
            if self.hits[m] <= timestamp and (m == len(self.hits) - 1 or self.hits[m + 1] > timestamp):
                v2 = m + 1
                break
            elif self.hits[m] > timestamp:
                r = m - 1
            else:
                l = m + 1
        if v2 == -1:
            return 0
        if timestamp < 300:
            return v2
        v1 = -1
        l = 0
        r = len(self.hits) - 1
        while l <= r:
            m = (l + r) // 2
            if self.hits[m] >= timestamp - 299 and (m == 0 or self.hits[m - 1] < timestamp - 299):
                v1 = m + 1
                break
            elif self.hits[m] < timestamp - 299:
                l = m + 1
            else:
                r = m - 1
        if v1 == -1:
            return 0
        return v2 - v1 + 1


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)