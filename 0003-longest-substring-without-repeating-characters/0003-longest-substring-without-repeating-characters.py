class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxcount=0
        charlist=set()
        l=0
        for r in range(len(s)):
            # if same char present in charlist, move l unitil it removes 
            while s[r] in charlist:
                charlist.remove(s[l])
                l+=1
            charlist.add(s[r])
            maxcount=max(maxcount,r-l+1)
        return maxcount        

        