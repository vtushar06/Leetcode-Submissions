class Solution(object):
    def lengthOfLastWord(self, s):
        lis=s.strip().split(" ")
        
        lastword=lis[-1]
        return (len(lastword))
        