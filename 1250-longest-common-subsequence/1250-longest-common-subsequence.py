class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1]*1001 for i in range(1001)]
        def solve(i,j):
            if i==n or j==m:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            ans=0    
            if text1[i]==text2[j]:
                ans=1+solve(i+1,j+1)
            else:
                ans=max(solve(i+1,j),solve(i,j+1))
            dp[i][j]=ans
            return dp[i][j]
        return solve(0,0)           

        