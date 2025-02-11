class Solution(object):
    def splitArray(self, nums, k):
        def countsubarray(nums,mid):
            count=1
            sum1=0
            for num in nums:
                if num+sum1>mid:
                    count+=1
                    sum1=num
                else:
                    sum1+=num
            return count            
        low,high=max(nums),sum(nums)
        ans=high
        while(low<=high):
            mid=(low+high)//2
            counter=countsubarray(nums,mid)
            if counter>k:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans            
        