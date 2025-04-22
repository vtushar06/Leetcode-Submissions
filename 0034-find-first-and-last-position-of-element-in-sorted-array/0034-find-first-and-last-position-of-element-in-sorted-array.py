class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def Lowerbound(nums,target):
            n=len(nums)
            low=0
            high=n-1
            ans=-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]>=target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans  
        def Upperbound(nums,target):
            n=len(nums)
            low=0
            high=n-1
            ans=-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]>target:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans-1 if ans!=-1 else n-1   
        
        
        lower=Lowerbound(nums,target)
        if lower==-1:return [-1,-1]
        upper=Upperbound(nums,target)
        if (upper==len(nums) or nums[upper]!=target):
            return [-1,-1]
        else:
            return [lower,upper]    




               

