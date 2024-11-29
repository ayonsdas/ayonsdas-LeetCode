class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        x = []
        for i in range(1, n + 1):
            if i % 5 and i % 3:
                x.append(str(i))
                continue
            if i % 5:
                x.append("Fizz")
                continue
            if i % 3:
                x.append("Buzz")
                continue
            x.append("FizzBuzz")
        return x