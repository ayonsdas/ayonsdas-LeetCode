class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        a = m = 0
        first = defaultdict(int)
        for i in range(len(hours)):
            if not a in first:
                first[a] = i
                
            if hours[i] > 8:
                a += 1
            else:
                a -= 1
            if a - 1 in first:
                m = max(m, i + 1 - first[a - 1], i + 1 if a > 0 else 0)
        return m