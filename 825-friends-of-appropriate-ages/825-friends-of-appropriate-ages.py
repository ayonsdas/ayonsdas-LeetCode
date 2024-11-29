class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ageStuff = [0 for _ in range(121)]
        for age in ages:
            ageStuff[age] += 1
        for i in range(2, 121):
            ageStuff[i] += ageStuff[i - 1]
        c = 0
        for i in ages:
            c += max(0, ageStuff[i] - ageStuff[int(i * .5) + 7] - 1)
        return c