class Solution(object):
    def pivotIndex(self, nums):
        n=len(nums)
        for i in range(n):
            sum1=sum(nums[0:i])
            sum2=sum(nums[i+1:n+1])
            if sum1==sum2:
                return i
        return -1  
        