class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        l = [0]
        x = []
        for i in range(len(arr)):
            l.append(l[-1] ^ arr[i])
        for query in queries:
            x.append(l[query[1] + 1] ^ l[query[0]])
        return x