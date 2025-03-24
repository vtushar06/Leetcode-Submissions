class Solution(object):
    def rob(self, nums):
        n=len(nums)
        dp=[-1]*n
        def robnows(index,N):
            if index==N-1:return nums[index]
            if index==N-2:return max(nums[index],nums[index+1])
            if index>=N:return 0
            if dp[index] !=-1:return dp[index]
            way_1=nums[index]+robnows(index+2,N)
            way_2=robnows(index+1,N)
            dp[index]=max(way_1,way_2)
            return dp[index]
        return robnows(0,n)    
        