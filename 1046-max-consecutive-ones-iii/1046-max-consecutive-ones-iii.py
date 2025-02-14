class Solution(object):
    def longestOnes(self, nums, k):
        l,r=0,0
        zeros=0
        maxlength=0
        while(r<len(nums)):
            if nums[r]==0:zeros+=1
            if(zeros>k):
                if nums[l]==0:
                    zeros-=1
                l+=1
            if zeros<=k:
                maxlength=max(maxlength,r-l+1)
            r+=1
        return maxlength                
        