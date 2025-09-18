class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # If total sum is odd, cannot partition equally
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        
        # dp[w] = True if subset sum w is possible
        dp = [False] * (target + 1)
        dp[0] = True  # Base: sum 0 is always possible
        
        for num in nums:
            # Traverse backwards to avoid using the same number multiple times
            for w in range(target, num - 1, -1):
                dp[w] = dp[w] or dp[w - num]
        
        return dp[target]