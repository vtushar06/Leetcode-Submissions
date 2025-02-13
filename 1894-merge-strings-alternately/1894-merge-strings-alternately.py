class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i,j=0,0
        result=""
        while(i<len(word1) or j<len(word2)):
            ch1=word1[i] if i<len(word1) else ""
            ch2=word2[j] if j<len(word2) else ""
            result+=ch1+ch2
            i+=1
            j+=1
        return result    

        