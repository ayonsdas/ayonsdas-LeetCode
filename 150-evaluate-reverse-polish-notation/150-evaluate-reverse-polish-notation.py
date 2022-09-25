class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        v = "+-*/"
        for token in tokens:
            if not token in v:
                s.append(int(token))
            else:
                l = s[-2]
                r = s[-1]
                s = s[:-2]
                if token == '+':
                    s.append(l +  r)
                elif token == '-':
                    s.append(l -  r)
                elif token == '*':
                    s.append(l *  r)
                else:
                    if r < 0:
                        l, r = l *-1, r *-1
                    if l < 0 and l % r != 0:
                        l += r
                    s.append(l // r)
        return s[-1]