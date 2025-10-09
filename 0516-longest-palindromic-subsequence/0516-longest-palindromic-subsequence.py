class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp=[[-1]*1000 for i in range(1000)]
        def solve(i,j):
            if i>j:
                return 0
            if i==j:
                if(s[i]==s[j]):return 1
                else:return 0

            if dp[i][j]!=-1:
                return dp[i][j]
            ans1=ans2=0    
            if s[i]==s[j]:
                ans1=2+ solve(i+1,j-1)
            ans2=max(solve(i+1,j),solve(i,j-1))
            dp[i][j]=max(ans1,ans2)
            return dp[i][j]
        return solve(0,len(s)-1)        
                    
        