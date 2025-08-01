class Solution(object):
    def subarraySum(self, nums, k):
        currentsum=0
        l,r=0,0
        map={0:1}
        count=0
        while(r<len(nums)):
            currentsum+=nums[r]
            remainingsum=currentsum-k
            if remainingsum in map:
                count+=map[remainingsum]
            map[currentsum]=map.get(currentsum,0)+1
            r+=1
        return count       

