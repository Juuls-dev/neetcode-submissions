class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i, num in enumerate(nums):
            r = target - num

            if r in s:
                return [s[r], i]

            
            s[num] = i
        