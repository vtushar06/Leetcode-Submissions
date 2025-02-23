class Solution(object):
    def areOccurrencesEqual(self, s):
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        value=dic[s[0]]    
        values=dic.values()

        return True if all(value==value1 for value1 in values) else False
        