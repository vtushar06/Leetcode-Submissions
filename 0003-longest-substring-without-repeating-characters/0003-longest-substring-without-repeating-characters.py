class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength=0
        listchar=set()
        l=0
        for r in range(len(s)):
            while s[r] in listchar:
                listchar.remove(s[l])
                l+=1
            listchar.add(s[r])
            maxlength=max(maxlength,r-l+1)
        return maxlength        
                
 