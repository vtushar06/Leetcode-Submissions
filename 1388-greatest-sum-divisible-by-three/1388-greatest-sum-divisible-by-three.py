class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, 0, 0]  

        for num in nums:
            temp = dp[:]  # Copy current dp states
            for x in temp:
                remainder = (x + num) % 3
                dp[remainder] = max(dp[remainder], x + num)

        return dp[0]
        