class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        def isPalindrome(l,r):
            while(l<r):
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def backtrack(idx,curr):
            if idx==len(s):
                result.append(curr[:])
                return
            if idx>len(s):
                return
            for i in range(idx,len(s)):
                if(isPalindrome(idx,i)):
                    curr.append(s[idx:i+1])
                    backtrack(i+1,curr)
                    curr.pop()
        backtrack(0,[])
        return result                    

        