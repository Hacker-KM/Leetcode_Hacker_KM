class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                mp+=prices[i+1]-prices[i]
                print(mp)
        return mp