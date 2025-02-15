class Solution(object):
    def pivotInteger(self, n):
        prefixsum=[0]*(n+1)
        for i in range(1,n+1):
            prefixsum[i]=prefixsum[i-1]+i
        
        for i in range(1,n+1):
            leftsum=prefixsum[i-1]
            rightsum=prefixsum[n]-prefixsum[i]
            if leftsum==rightsum:
                return i
        return -1        


        
        