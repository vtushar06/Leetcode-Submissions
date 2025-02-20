class Solution(object):
    def isPalindrome(self, s):
        string=""
        reverse=""
       
        for i in range(len(s)):
            if s[i].isalpha():
                string=string+s[i].lower()
                reverse=s[i].lower()+reverse
            if s[i].isdigit():
                string=string+s[i] 
                reverse=s[i]+reverse   
        if string==reverse:return True
        return False        
