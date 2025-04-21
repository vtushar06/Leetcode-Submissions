class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expectedsum=n*(n+1)//2
        actualsum=sum(nums)
        return expectedsum-actualsum
        
        
        
        
        
        
        
        
        
        # s=sum(nums)
        # n=len(nums)
        # S=sum(range(0,n+1))
        # missingnumber=S-s
        # return missingnumber
        