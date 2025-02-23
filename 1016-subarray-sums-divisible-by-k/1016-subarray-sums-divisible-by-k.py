class Solution(object):
    def subarraysDivByK(self, nums, k):
        dic={0:1}
        count=0
        prefixsum=0
        for num in nums:
            prefixsum+=num
            remainder=prefixsum%k
            if remainder in dic:
                count+=dic[remainder]
            dic[remainder]=dic.get(remainder,0)+1    
        return count    