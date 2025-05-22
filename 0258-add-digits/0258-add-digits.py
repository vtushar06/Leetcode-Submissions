class Solution:
    def addDigits(self, num: int) -> int:
        ans=0
        while(num>9):
            n=num
            
            while(n!=0):
                a=n%10
                ans+=a
                n=n//10
            num=ans
            ans=0
        return num        
        