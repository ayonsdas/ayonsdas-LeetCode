class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.i = 0
        self.discount = discount
        self.k = {}
        for i in range(len(products)):
            self.k[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.i += 1
        d = False
        if self.i == self.n:
            d = True
            self.i = 0
        t = 0
        for i in range(len(product)):
            t += self.k[product[i]] * amount[i]
        if d:
            t *= (100 - self.discount) / 100
        return t

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product, amount)