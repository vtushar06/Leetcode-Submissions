class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = [0] * (len(nums) + 1)  # Extra space for easier calculations
        
        # Precompute prefix sums
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix_sum[right + 1] - self.prefix_sum[left]