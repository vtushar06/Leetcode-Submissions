class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lis=s.split(" ")[:k]
        return " ".join(lis)
        
        