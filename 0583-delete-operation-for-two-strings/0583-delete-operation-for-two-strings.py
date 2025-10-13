class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
            n=len(word1)
            m=len(word2)
            dp=[[-1]*500 for i in range(500)]
            def solve(i,j):
                if i==n:
                    return m-j
                if j==m:
                    return n-i
                if dp[i][j]!=-1:
                    return dp[i][j]
                ans=0
                if (word1[i]==word2[j]):
                    ans=solve(i+1,j+1)
                else:
                    deleteword1=1+solve(i+1,j)
                    deleteword2=1+solve(i,j+1)
                    ans=min(deleteword1,deleteword2)
                dp[i][j]=ans
                return ans
            return solve(0,0) 