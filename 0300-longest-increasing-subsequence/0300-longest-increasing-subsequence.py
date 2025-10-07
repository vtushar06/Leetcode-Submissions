class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1]*n for i in range(n)]
        def solve(i,prev):
            if i==n:
                return 0
            if dp[i][prev] !=-1:
                return dp[i][prev]
            take=nottake=0
            if(nums[prev]<nums[i] or prev==-1):
                take=1+solve(i+1,i)
            nottake=solve(i+1,prev)
            dp[i][prev]=max(take,nottake)
            return dp[i][prev]
        return max(1+solve(1,0), solve(1,-1))              
        