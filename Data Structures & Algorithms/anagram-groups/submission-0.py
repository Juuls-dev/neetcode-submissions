from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
         
        for w in strs:
            word = ''.join(sorted(w))
            hash[word].append(w)
        return list(hash.values())