class Solution:
    def originalDigits(self, s: str) -> str:
        s = Counter(s)
        t = [0 for _ in range(10)]
        t[0] = s['z']
        t[6] = s['x']
        t[8] = s['g']
        t[4] = s['u']
        t[2] = s['w']
        t[7] = s['s'] - t[6]
        t[3] = s['h'] - t[8]
        t[5] = s['f'] - t[4]
        t[1] = s['o'] - t[0] - t[2] - t[4]
        t[9] = s['i'] - t[5] - t[8] - t[6]
        return "".join([str(i) * t[i] for i in range(len(t))])