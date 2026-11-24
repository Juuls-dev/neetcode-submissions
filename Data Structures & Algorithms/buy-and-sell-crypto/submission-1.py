class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rm = prices[0]
        dif =0
        for t in prices:
            dif = max(dif, t - rm)
            rm = min(t,rm)

        return dif
