class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        def f(i,n):
            if i>=n-1:
                return 0

            if dp[i]!=-1:
                return dp[i]
            min_steps=float("inf")
            for j in range(1,nums[i]+1):
                if i+j<n:
                    jump_j=1+f(i+j,n)  
                    min_steps=min(min_steps,jump_j)
            dp[i]=min_steps
            return dp[i]
        return f(0,n)            


        