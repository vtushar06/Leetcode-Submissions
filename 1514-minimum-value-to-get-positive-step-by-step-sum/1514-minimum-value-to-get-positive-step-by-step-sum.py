class Solution(object):
    def minStartValue(self, nums):
        runningsum=0
        minimumsum=0
        for num in nums:
            runningsum+=num
            minimumsum=min(minimumsum,runningsum)
        return 1- minimumsum if minimumsum<0 else 1