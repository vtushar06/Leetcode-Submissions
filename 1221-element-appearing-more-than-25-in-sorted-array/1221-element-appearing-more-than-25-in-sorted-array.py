class Solution(object):
    def findSpecialInteger(self, arr):
        def lower(arr,k):
            low,high=0,len(arr)-1
            ans=-1
            while(low<=high):
                mid=(low+high)//2
                if arr[mid]>=k:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans  
     
        def higher(arr,k):
            low,high=0,len(arr)-1
            ans=len(arr)
            while(low<=high):
                mid=(low+high)//2
                if arr[mid]>k:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans  

        nums=set(arr)
        for num in nums:
            l=lower(arr,num)
            h=higher(arr,num)
            count=h-l
            if count>len(arr)/4:
                return num   
        return -1                      


        