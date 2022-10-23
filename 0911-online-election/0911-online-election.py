class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        a = max(persons)
        x = [0 for _ in range(a + 1)]
        self.l = []
        leader = -1
        mScore = 0
        for p in persons:
            x[p] += 1
            if x[p] >= mScore:
                mScore = x[p]
                leader = p
            self.l.append(leader)
        print(self.l)

    def q(self, t: int) -> int:
        return self.l[bisect.bisect_right(self.times, t) - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)