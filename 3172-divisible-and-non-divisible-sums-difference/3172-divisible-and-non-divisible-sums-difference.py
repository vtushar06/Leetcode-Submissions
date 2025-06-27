class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        k = n // m
        divisible_sum = m * (k * (k + 1) // 2)
        non_divisible_sum = total - divisible_sum
        return non_divisible_sum - divisible_sum