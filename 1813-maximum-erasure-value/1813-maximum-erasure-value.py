class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        seen=set()
        currsum=0
        maxsum=float("-inf")
        l,r=0,0
        while(r<n):
            while(nums[r] in seen):
                seen.remove(nums[l])
                currsum-=nums[l]
                l+=1
            seen.add(nums[r])
            currsum+=nums[r]
            maxsum=max(maxsum,currsum)
            r+=1
        return maxsum        

        