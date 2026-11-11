class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        ma=0

        for n in num:
            if (n- 1) not in num:
                l=1
                while (n+l) in num:
                    l+=1
                ma = max(l,ma)
        return ma

