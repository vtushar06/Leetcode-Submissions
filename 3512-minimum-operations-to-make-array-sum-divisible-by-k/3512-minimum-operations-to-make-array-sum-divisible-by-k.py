class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        total = sum(nums)
        rem = total % k
        return rem