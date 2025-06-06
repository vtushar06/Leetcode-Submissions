class Solution:
    def reverseVowels(self, s: str) -> str:
        lis=[]
        pos=[]
        vowels="aeiouAEIOU"
        
        for i in range(len(s)):
            if s[i] in vowels:
                lis.append(s[i])
                pos.append(i)
        lis.reverse()
        st=list(s)
        for j in range(len(pos)):
            st[pos[j]]=lis[j]
            j+=1
        return "".join(st)    
                 
        