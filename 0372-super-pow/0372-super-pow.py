class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = int("".join(map(str, b)))
        def supPow(a: int, b: int) -> int:
            if b == 0:
                return 1
            if b % 2:
                l = supPow(a, b // 2)
                return (l ** 2 * a) % 1337
            l = supPow(a, b // 2)
            return (l ** 2) % 1337
        
        return supPow(a, b)