class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        obj={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def backtrack(i,path):
            if len(path)==len(digits):
                ans.append(path)
                return
            for ch in obj[digits[i]]:
                backtrack(i+1,path+ch)
        if len(digits)==0:
            return []        
        backtrack(0,"")
        return ans           
        