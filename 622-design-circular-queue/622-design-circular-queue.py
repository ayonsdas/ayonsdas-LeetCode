class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.currSize = 0
        self.queue = []

    def enQueue(self, value: int) -> bool:
        if self.currSize == self.size:
            return False
        self.queue.append(value)
        self.currSize += 1
        return True

    def deQueue(self) -> bool:
        if self.currSize == 0:
            return False
        self.queue.pop(0)
        self.currSize -= 1
        return True

    def Front(self) -> int:
        return self.queue[0] if self.currSize else -1

    def Rear(self) -> int:
        return self.queue[-1] if self.currSize else -1

    def isEmpty(self) -> bool:
        return self.currSize == 0

    def isFull(self) -> bool:
        return self.currSize == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()