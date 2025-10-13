class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp=[[-1]*1000 for i in range(1000)]
        nums.sort()
        n=len(nums)
        def solve(i,prev):
            if i==n:
                return []
            if dp[i][prev]!=-1:
                return dp[i][prev]
            #take
            take=nottake=[] 
            if (nums[i]%nums[prev]==0) or prev==-1:
                take=[nums[i]]+solve(i+1,i)
            nottake=solve(i+1,prev)
            if len(take)>len(nottake):
                dp[i][prev]=take
            else:
                dp[i][prev]=nottake
            return dp[i][prev]
        #include first
        ans1=[nums[0]]+solve(1,0)
        #not include first
        ans2=solve(1,-1)
        return ans1 if len(ans1)>len(ans2) else ans2            

        