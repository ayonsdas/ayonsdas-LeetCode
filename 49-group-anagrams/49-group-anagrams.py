class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        for st in strs:
            x = "".join(sorted([char for char in st]))
            if not x in keys:
                keys[x] = []
            keys[x].append(st)
        return list(keys.values())