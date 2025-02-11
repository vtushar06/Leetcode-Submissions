class Solution(object):
    def findKthPositive(self, arr, k):
        low,high=0,len(arr)-1
        while(low<=high):
            mid=low+(high-low)//2
            kitna_missing_number_at_mid=arr[mid]-(mid+1)

            if kitna_missing_number_at_mid<k:
                low=mid+1
            else:
                high=mid-1

        return (low+k)            
        