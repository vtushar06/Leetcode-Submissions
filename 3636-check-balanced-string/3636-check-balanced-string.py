class Solution:
    def isBalanced(self, num: str) -> bool:
        n = len(num)
        even = sum(int(num[i]) for i in range(1, n, 2))
        odd = sum(int(num[i]) for i in range(0, n, 2))
        return even == odd
        