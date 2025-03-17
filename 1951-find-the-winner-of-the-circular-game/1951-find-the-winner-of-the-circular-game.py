class Solution(object):
    def findTheWinner(self, n, k):
        winner = 0  # Josephus(1, k) = 0 (0-based index)
        
        for i in range(2, n + 1):
            winner = (winner + k) % i
        
        return winner + 1
        