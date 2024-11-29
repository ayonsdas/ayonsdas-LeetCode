class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
        b = 0
        secret = Counter(secret)
        guess = Counter(guess)
        for l in secret:
            b += min(secret[l], guess[l])
        b -= a
        return "{}A{}B".format(a, b)