class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        def gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        common=gcd(a,b)
        count=0
        for i in range(1,common+1):
            if common%i==0:
                count+=1
        return count        

