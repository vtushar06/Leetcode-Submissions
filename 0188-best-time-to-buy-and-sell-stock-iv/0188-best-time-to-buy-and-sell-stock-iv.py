class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(len(prices))]

        def solve(idx,canbuy,cap):
            if cap==0 or idx==len(prices):
                return 0
            if dp[idx][canbuy][cap]!=-1:
                return dp[idx][canbuy][cap]    
            if (canbuy):
                buy=-prices[idx]+solve(idx+1,0,cap)
                notbuy=solve(idx+1,1,cap)
                profit=max(buy,notbuy)
            else:
                sell=+prices[idx]+solve(idx+1,1,cap-1)
                notsell=solve(idx+1,0,cap)
                profit=max(sell,notsell)
            dp[idx][canbuy][cap] = profit
            return dp[idx][canbuy][cap] 

        return solve(0,1,k) 
        