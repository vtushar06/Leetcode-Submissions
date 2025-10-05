class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp=[[-1]*m for i in range(n)]
        def solve(i,j):
            if j==m:
                return 1
            if i>=n:
                return 0 
            if dp[i][j]!=-1:
                return dp[i][j]         
            ans=0
            if(s[i]==t[j]):
                ans+=solve(i+1,j+1)

            ans+=solve(i+1,j)
            dp[i][j]=ans
            return dp[i][j]
            
        return solve(0,0)            

        