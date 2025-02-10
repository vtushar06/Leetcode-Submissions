class Solution(object):
    def myPow(self, x, n):
        ans=1
        m=n
        n=abs(n)
        while(n>0):
            if n%2!=0:
                ans*=x
                n=n-1
            else:
                x=x*x
                n=n//2
        return ans if m>0 else 1/ans            
        