class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}:{s}' for s in strs)
    def decode(self, s: str) -> List[str]:
        res =[]
        i =0
        while i < len(s):
            j = s.find(':',i)
            l = int(s[i:j])
            start = j+1
            end = start + l
            res.append(s[start:end])
            i = end
        return res