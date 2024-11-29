class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks = Counter(tasks)
        l = 0
        for task in tasks:
            if tasks[task] == 1:
                return -1
            if tasks[task] % 3 == 0:
                l += tasks[task] // 3
            else:
                l += tasks[task] // 3 + 1
        return l