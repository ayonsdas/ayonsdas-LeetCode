class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        s = defaultdict(list)
        for string in strings:
            l = 0
            for i in range(1, len(string)):
                l *= 26
                j = (ord(string[i]) - ord(string[i - 1])) % 26
                if j == 0:
                    j = 26
                l += j
            s[l].append(string)
        return [s[a] for a in s]