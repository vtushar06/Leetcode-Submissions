from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxindex=0
        for i in range(0,len(nums)):
            if i>maxindex:return False
            maxindex=max(maxindex,i+nums[i])
        return True    




        
        # dp=[-1]*(len(nums)+1)
        # def jump(nums,i):
        #     if i==0: return True
        #     if i<0:return False

        #     if dp[i] !=-1:return dp[i]

         
        #     for j in range(1,nums[i]+1):
        #         if i-j>0:
        #             steps=jump(nums,i-j)
                   
        #     dp[i]= maxsteps
        #     return dp[i]   
        # return jump(nums,len(nums)-1) 