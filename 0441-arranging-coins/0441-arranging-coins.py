class Solution:
    def arrangeCoins(self, n: int) -> int:
        low,high=0,n
        ans=high
        while(low<=high):
            k=(low+high)//2
            if (k*(k+1))//2<=n:
                ans=k
                low=k+1
            else:
                high=k-1
        return ans            
        