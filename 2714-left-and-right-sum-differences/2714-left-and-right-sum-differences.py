class Solution(object):
    def leftRightDifference(self, nums):
        n=len(nums)
        result=[]
        prefixsum=[0]*n
        prefixsum[0]=nums[0]
        for i in range(1,n):
            prefixsum[i]=prefixsum[i-1]+nums[i]
        suffixsum=[0]*n 
        suffixsum[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            suffixsum[i]=suffixsum[i+1]+nums[i]
        for i in range(n):
            absdiff=abs(prefixsum[i]-suffixsum[i])
            result.append(absdiff)  
        return result     


        