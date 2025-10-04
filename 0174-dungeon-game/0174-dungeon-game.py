class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
            m=len(dungeon)
            n=len(dungeon[0])
            dp=[[-1]*n for i in range(m)]
            def solve(i,j):
                if i==m-1 and j==n-1:
                    if dungeon[i][j]<=0:
                        return abs(dungeon[i][j])+1
                    else:
                        return 1
                if dp[i][j]!=-1:
                    return dp[i][j] 
                right=down=float("inf")    
                if j+1<n:
                    right=solve(i,j+1)
                if i+1<m:
                    down=solve(i+1,j)
                minimumrequired=min(right,down)
                result=minimumrequired-(dungeon[i][j])

                dp[i][j]=result if result>0 else 1
                return dp[i][j]
            return solve(0,0)    