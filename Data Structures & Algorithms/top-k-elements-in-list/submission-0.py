from collections import Counter
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        buckets = defaultdict(list)

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result
