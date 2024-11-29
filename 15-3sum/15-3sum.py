class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counts = {}
        trips = []
        for t in nums:
            if not t in counts:
                counts[t] = 1
            else:
                counts[t] += 1
        vals = sorted(list(counts))
        for i in range(len(vals) - 1):
            used = {}
            for j in range(i, len(vals)):
                if not vals[j] in used and vals[j] >= vals[i]:
                    if i == j and counts[vals[i]] == 1:
                        continue
                    if vals[i] == 0 and vals[j] == 0:
                        if counts[0] >= 3:
                            trips.append([0, 0, 0])
                    else:
                        t = (vals[i] + vals[j]) * -1
                        if t in counts and t >= vals[i] and t >= vals[j]:
                            if vals[i] == t and counts[t] >= 2:
                                trips.append([vals[i], vals[j], t])
                                used[t] = ''
                            if vals[j] == t and counts[t] >= 2:
                                trips.append([vals[i], vals[j], t])
                                used[t] = ''
                            if vals[i] != t and vals[j] != t:
                                trips.append([vals[i], vals[j], t])
                                used[t] = ''
        if len(vals) == 1:
            if vals[0] == 0 and counts[0] >= 3:
                trips.append([0, 0, 0])
        return trips