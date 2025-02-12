class Solution:
    def climbStairs(self, n: int,memo={}) -> int:
        if n in memo:
            return memo[n]
        if n==1 or n==2:
            return n
        stair_1=self.climbStairs(n-1,memo)   
        stair_2=self.climbStairs(n-2,memo)   
        memo[n]=stair_1+stair_2
        return memo[n]