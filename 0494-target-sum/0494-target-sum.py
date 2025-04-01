class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}

        def dfs(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in memo:
                return memo[(index, total)]

        # Choose '+' or '-'
            memo[(index, total)] = dfs(index + 1, total + nums[index]) + dfs (index + 1, total - nums[index])
            return memo[(index, total)]

        return dfs(0, 0)

        