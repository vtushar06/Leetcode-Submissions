class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def isvalid(time,totalTrips,mid):
            trips=0
            for i in range(len(time)):
                trips+=mid//time[i]
            if trips>=totalTrips:return True
            else:return False  
        low,high=1,min(time)*totalTrips
        ans=high
        while(low<=high):
            mid=low+(high-low)//2
            if (isvalid(time,totalTrips,mid)):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans                       