class Solution:
    def alternatingSum(self, nums):
        total = 0
        for i, x in enumerate(nums):
            if i % 2 == 0:
                total += x
            else:
                total -= x
        return total