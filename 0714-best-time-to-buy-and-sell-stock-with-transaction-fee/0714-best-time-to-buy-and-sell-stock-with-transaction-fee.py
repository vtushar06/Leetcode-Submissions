class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp=[[-1]*2 for i in range(len(prices))]
    
        def solve(idx,canbuy):
            if idx==len(prices):
                return 0
            if dp[idx][canbuy]!=-1:
                return dp[idx][canbuy]

            if (canbuy):
                # is index pa ma pocket sa de raha hu tuo minus kiys and solve function ko kha raha hu ki bhai
                # jo aaga sa profit ho vo lekar aah ja
                buy=-prices[idx]+solve(idx+1,0)
                # agar mana buy nahi kiya tuo mana solve function ko bola bhai 
                # aaga sa jitna bhi profit ha leakr aah ja
                notbuy=solve(idx+1,1) 

                profit=max(buy,notbuy)   
            else:
                sell=prices[idx]-fee+solve(idx+1,1)

                notsell=solve(idx+1,0)

                profit=max(sell,notsell)

            dp[idx][canbuy]= profit
            return profit

        return solve(0,1)