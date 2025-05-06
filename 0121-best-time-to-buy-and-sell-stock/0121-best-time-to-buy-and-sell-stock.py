class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        maxprofit=0
        for price in prices:
            profit=price-mini
            maxprofit=max(profit,maxprofit)
            mini=min(mini,price)
        return maxprofit    
        