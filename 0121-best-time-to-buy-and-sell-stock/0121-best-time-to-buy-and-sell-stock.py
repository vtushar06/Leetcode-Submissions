class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mincost=float("inf")
        maxcost=0
        for price in prices:
            mincost=min(mincost,price)
            maxcost=max(maxcost,price-mincost)
        return maxcost    
        