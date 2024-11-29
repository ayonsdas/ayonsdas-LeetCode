import random

class RandomizedSet:

    def __init__(self):
        self.key = set()

    def insert(self, val: int) -> bool:
        if val in self.key:
            return False
        self.key.add(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.key:
            return False
        self.key.remove(val)
        return True

    def getRandom(self) -> int:
        t = list(self.key)
        k = random.randint(0, len(t) - 1)
        return t[k]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()