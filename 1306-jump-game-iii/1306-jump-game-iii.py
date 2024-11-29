class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visited = set()
        q = [start]
        while q:
            t = q.pop(0)
            if arr[t] == 0:
                return True
            visited.add(t)
            if t + arr[t] < len(arr) and (t + arr[t]) not in visited:
                q.append(t + arr[t])
            if t - arr[t] >= 0       and (t - arr[t]) not in visited:
                q.append(t - arr[t])
        return False