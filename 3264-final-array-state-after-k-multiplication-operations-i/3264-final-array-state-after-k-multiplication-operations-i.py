class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            miniidx=-1
            mini=1000000
            for i in range(len(nums)):
                if nums[i]<mini:
                    mini=nums[i]
                    miniidx=i
            nums[miniidx]=nums[miniidx]*multiplier
        return nums           
        