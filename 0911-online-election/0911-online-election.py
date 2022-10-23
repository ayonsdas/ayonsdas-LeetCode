class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        a = max(persons)
        x = {}
        self.l = [-1 for _ in range(len(times))] 
        leader = -1
        mScore = 0
        i = 0
        for p in persons:
            if not p in x:
                x[p] = 0
            x[p] += 1
            if x[p] >= mScore:
                mScore = x[p]
                leader = p
            self.l[i] = leader
            i += 1

    def q(self, t: int) -> int:
        return self.l[bisect.bisect_right(self.times, t) - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)