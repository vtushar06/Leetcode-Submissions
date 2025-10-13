class Solution:
    def minInsertions(self, s: str) -> int:
            n=len(s)
            dp=[[-1]*500 for i in range(500)]
            def solve(i,j):
                if i==j:
                    return 0
                if i>j:
                    return 0
                if dp[i][j]!=-1:
                    return dp[i][j]
                ans=0
                if (s[i]==s[j]):
                    ans=solve(i+1,j-1)
                else:
                    leftinsert=1+solve(i,j-1)  
                    rightinsert=1+solve(i+1,j)
                    ans=min(leftinsert,rightinsert) 
                dp[i][j]=ans
                return ans
            return solve(0,n-1) 