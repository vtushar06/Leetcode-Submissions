class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={0:1}
        currsum=0
        count=0
        for num in nums:
            currsum+=num
            remaining=currsum-k
            if remaining in dic:
                count+=dic[remaining]
            dic[currsum]=dic.get(currsum,0)+1  
        return count      
