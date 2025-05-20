class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_linear(houses):
            prev, curr = 0, 0
            for money in houses:
                prev, curr = curr, max(curr, prev + money)
            return curr

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))