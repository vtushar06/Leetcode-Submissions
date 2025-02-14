class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        presum={0:1}
        currentsum=0
        count=0
        for num in nums:
            currentsum+=num
            remaining=currentsum-goal
            if remaining in presum:
                count+=presum[remaining]
            presum[currentsum]=presum.get(currentsum,0)+1
        return count        