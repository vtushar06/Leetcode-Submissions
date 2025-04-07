class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
            num1=num
            if num1==1:return False
            sum1=1
            for i in range(2,int(num**0.5)+1):
                if num1%i==0:
                    a=num1//i
                    sum1+=i+a 
            return sum1==num1               