class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        t = []
        x = Counter(target)
        for i in range(1, min(target[-1], n) + 1):
            t.append("Push")
            if not i in x:
                t.append("Pop")
        return t