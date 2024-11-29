class DN:
    
    def __init__(self, vl, pre, nex):
        self.val = vl
        self.prev = pre
        self.next = nex

class MyLinkedList:

    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

        
    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        temp = self.front
        for i in range(index):
            temp = temp.next
        return temp.val

    
    def addAtHead(self, val: int) -> None:
        self.front = DN(val, None, self.front)
        if self.back:
            self.front.next.prev = self.front
        else:
            self.back = self.front
        self.size += 1
        temp = self.front


    def addAtTail(self, val: int) -> None:
        self.back = DN(val, self.back, None)
        if self.front:
            self.back.prev.next = self.back
        else:
            self.front = self.back
        self.size += 1
        temp = self.front


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        temp = self.front
        for i in range(index):
            temp = temp.next
        curr = DN(val, temp.prev, temp)
        temp.prev.next = curr
        temp.prev = curr
        self.size += 1
        temp = self.front

        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.front = self.front.next
            if self.front:
                self.front.prev = None
            else:
                self.back = None
        elif index == self.size - 1:
            self.back = self.back.prev
            if self.back:
                self.back.next = None
            else:
                self.front = None
        else:
            temp = self.front
            for i in range(index):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)