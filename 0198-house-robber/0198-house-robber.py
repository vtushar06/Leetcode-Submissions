class Solution(object):
    def rob(self, nums):
        n=len(nums)
        dp={}
        if n==1: return nums[0]
        dp[0]=nums[0]
        for i in range(1,n):
            take=nums[i]+(dp[i-2] if i>1 else 0)
            nottake=0+dp[i-1]
            dp[i]=max(take,nottake)
        return dp[n-1]

        # n=len(nums)
        # dp=[-1]*n
        # def robnows(index,N):
        #     if index==N-1:return nums[index]
        #     if index==N-2:return max(nums[index],nums[index+1])
        #     if index>=N:return 0
        #     if dp[index] !=-1:return dp[index]
        #     way_1=nums[index]+robnows(index+2,N)
        #     way_2=robnows(index+1,N)
        #     dp[index]=max(way_1,way_2)
        #     return dp[index]
        # return robnows(0,n)    
        