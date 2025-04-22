class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isvalid(weights,days,mid):
            sum1=0
            d=1
            for i in range(len(weights)):
                sum1+=weights[i]
                if sum1>mid:
                    d+=1
                    sum1=weights[i]
                    
            if d<=days:
                return True
            else:
                return False            
        low,high=max(weights),sum(weights)
        ans=high
        while(low<=high):
            mid=(low+high)//2
            if(isvalid(weights,days,mid)):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans            

