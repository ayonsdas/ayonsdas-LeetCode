class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr = Counter(arr)
        c = -1
        for key in arr:
            if arr[key] == key:
                c = max(c, key)
        return c