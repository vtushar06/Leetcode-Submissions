class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[-1]*2 for i in range(len(prices))]
        def solve(idx,canbuy):
            if idx==len(prices):
                return 0
            if dp[idx][canbuy]!=-1:
                return  dp[idx][canbuy]
            if canbuy:
                buy=-prices[idx]+solve(idx+1,0)
                notbuy=solve(idx+1,1)
                profit=max(buy,notbuy)
            else:
                sell=prices[idx]+solve(idx+1,1)
                notsell=solve(idx+1,0)
                profit=max(sell,notsell)
            dp[idx][canbuy]=profit 
            return profit
        return solve(0,1)                  
        