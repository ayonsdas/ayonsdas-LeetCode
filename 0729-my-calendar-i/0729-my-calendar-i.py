class MyCalendar:

    def __init__(self):
        self.x = []

    def book(self, start: int, end: int) -> bool:
        for a in self.x:
            if a[1] > start and a[1] <= end or a[0] < end and a[0] >= start or end > a[0] and end <= a[1] or start < a[1] and start >= a[0]:
                return False
        self.x.append([start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)