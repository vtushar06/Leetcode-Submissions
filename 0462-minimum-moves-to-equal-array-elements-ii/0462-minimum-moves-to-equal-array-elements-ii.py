class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        middle=nums[len(nums)//2]
        moves=0
        for i in range(len(nums)):
            moves+=abs(nums[i]-middle)
        return moves    
        