class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringnumber=str(x)
        l=len(stringnumber)-1
        low=0
        high=l
        while(low<=high):
            if stringnumber[low]!=stringnumber[high]:
                return False
            else:
                low+=1
                high-=1
        return True            

        