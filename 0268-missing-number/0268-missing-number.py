class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        expectedsum=n*(n+1)//2
        actualsum=sum(nums)
        return expectedsum-actualsum
        