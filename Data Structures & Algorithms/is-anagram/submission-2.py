class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        counts2 = {}

        for char in t:
            counts2[char] = counts2.get(char, 0) + 1
        return counts == counts2
        