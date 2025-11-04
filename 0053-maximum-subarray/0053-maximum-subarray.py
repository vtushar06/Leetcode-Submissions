class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r=0
        currentsum=0 
        maxsum=float("-inf")
        while(r<len(nums)):
            currentsum+=nums[r]
            if maxsum<currentsum:
                maxsum=currentsum
            if currentsum<0:
                currentsum=0
            
            r+=1   
        return maxsum    