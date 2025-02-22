class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()
        ans=[]
        for q in queries:
            maxlength=0
            count=0
            sum1=0
            for n in nums:
                sum1+=n
                
                if sum1<=q:
                    count+=1
                    maxlength=max(count,maxlength)
            ans.append(maxlength)
        return ans            