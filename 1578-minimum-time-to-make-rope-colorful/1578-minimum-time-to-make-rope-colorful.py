class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        c = colors[0]
        s = neededTime[0]
        m = neededTime[0]
        r = 0
        i = 1
        while i < len(colors):
            if colors[i] == c:
                s += neededTime[i]
                m = max(m, neededTime[i])
            else:
                r += s - m
                c = colors[i]
                s = neededTime[i]
                m = neededTime[i]
            i += 1
        r += s - m
        return r