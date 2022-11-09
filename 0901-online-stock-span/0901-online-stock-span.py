class StockSpanner(object):

    def __init__(self):
        self.mStack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """

        res = 1
        while self.mStack and self.mStack[-1][0] <= price:
            res += self.mStack.pop()[1]
        self.mStack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)