class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        a = sorted([(plantTime[i], growTime[i]) for i in range(len(plantTime))], key = lambda x : -x[1])
        good = time = 0
        for i in range(len(a)):
            time += a[i][0]
            good = max(good, time + a[i][1])
        return good