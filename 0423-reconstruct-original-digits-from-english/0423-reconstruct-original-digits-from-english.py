class Solution:
    def originalDigits(self, s: str) -> str:
        s = Counter(s)
        t = [0 for _ in range(10)]
        while s['z'] > 0:
            t[0] += 1
            s['z'] -= 1
            s['e'] -= 1
            s['r'] -= 1
            s['o'] -= 1
        while s['g'] > 0:
            t[8] += 1
            s['e'] -= 1
            s['i'] -= 1
            s['g'] -= 1
            s['h'] -= 1
            s['t'] -= 1
        while s['h'] > 0:
            t[3] += 1
            s['t'] -= 1
            s['h'] -= 1
            s['r'] -= 1
            s['e'] -= 2
        while s['x'] > 0:
            t[6] += 1
            s['s'] -= 1
            s['i'] -= 1
            s['x'] -= 1
        while s['u'] > 0:
            t[4] += 1
            s['f'] -= 1
            s['o'] -= 1
            s['u'] -= 1
            s['r'] -= 1
        while s['f'] > 0:
            t[5] += 1
            s['f'] -= 1
            s['i'] -= 1
            s['v'] -= 1
            s['e'] -= 1
        while s['v'] > 0:
            t[7] += 1
            s['s'] -= 1
            s['v'] -= 1
            s['e'] -= 2
            s['n'] -= 1
        while s['i'] > 0:
            t[9] += 1
            s['n'] -= 2
            s['i'] -= 1
            s['e'] -= 1
        while s['t'] > 0:
            t[2] += 1
            s['t'] -= 1
            s['o'] -= 1
        while s['o'] > 0:
            t[1] += 1
            s['o'] -= 1
        return "".join([str(i) * t[i] for i in range(len(t))])