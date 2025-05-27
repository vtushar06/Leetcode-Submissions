class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort(reverse=True)
        
        ans=nums[2] if len(nums)>=3 else max(nums)
        return(ans)