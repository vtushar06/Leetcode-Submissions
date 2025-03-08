class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        i=0
        n=len(nums)
        maxi=0
        while(i<n-1):
            diff=nums[i+1]-nums[i] 
            maxi=max(maxi,diff)
            i+=1
        return maxi          