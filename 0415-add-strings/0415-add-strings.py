class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry=0
        i,j=len(num1)-1,len(num2)-1
        result=[]
        while( i>=0 or j>=0 or carry):
            n1=int(num1[i]) if i>=0 else 0
            n2=int(num2[j]) if j>=0 else 0
            total=n1+n2+carry
            carry=total//10
            a=total%10
            result.append(str(a))
            i-=1
            j-=1
        return "".join(reversed(result))    
