class Solution(object):
    def isHappy(self, n):
        
        def squaresum(a):
            sum1=0
            while(a!=0):
                b=a%10
                sum1+=b*b
                a=a//10
            return sum1
        seen=set() 
        while(n !=1 and n not in seen):
            seen.add(n)
            n=squaresum(n)
        return n==1 


            
        