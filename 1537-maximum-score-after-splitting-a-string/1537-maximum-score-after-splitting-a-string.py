class Solution(object):
    def maxScore(self, s):
        n=len(s)
        maxscore=-1
        prefixZero=[0]*n
        prefixZero[0]=(1 if s[0]=="0" else 0)
        for i in range(1,n):
            prefixZero[i]=prefixZero[i-1]+(1 if s[i]=="0" else 0)

        prefixOne=[0]*n
        prefixOne[n-1]=(1 if s[n-1]=="1" else 0)
        for i in range(n-2,-1,-1):
            prefixOne[i]=prefixOne[i+1]+(1 if s[i]=="1" else 0)

        for i in range(n-1):
            leftscore=prefixZero[i]
            rightscore=prefixOne[i+1]
            maxscore=max(maxscore,(leftscore+rightscore)) 
        return maxscore       
