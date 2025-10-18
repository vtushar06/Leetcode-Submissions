class Solution(object):
    def generateParenthesis(self, n):
        result=[]
        def generate(open,close,current):
            if len(current)==2*n:
                result.append(current)
                return
            if (open < n):
                generate(open+1,close,current+"(")
            if (close<open):
                generate(open,close+1,current+")")
        generate(0,0,"")
        return result

