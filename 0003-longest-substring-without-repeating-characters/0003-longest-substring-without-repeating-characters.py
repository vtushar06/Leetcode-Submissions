class Solution(object):
    def lengthOfLongestSubstring(self, string):
        l,r=0,0
        freq={}
        count=0
        while(r<len(string)):
            ch=string[r]
            if ch in freq:
                while(freq[ch]>0):
                    freq[string[l]]-=1
                    l+=1   
            count=max(count,r-l+1)
            freq[ch]=1
            r+=1
        return count        
        