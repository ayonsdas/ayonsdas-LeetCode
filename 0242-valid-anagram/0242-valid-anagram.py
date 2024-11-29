class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter([char for char in s]) == Counter([char for char in t])