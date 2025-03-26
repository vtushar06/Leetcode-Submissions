class Solution(object):
    def isThree(self, n):
        if n==1 or n==2:return False
        def count(x):
            count=0
            for i in range(1,x+1):
                if x%i==0:
                    count+=1
            return True if count==3 else False
        if count(n):return True
        return False            
        
        
        