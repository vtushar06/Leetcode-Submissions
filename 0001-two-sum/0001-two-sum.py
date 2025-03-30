class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexdic={}
        for i,num in enumerate(nums):
            remaining=target-num
            if remaining in indexdic.keys():
                return[i,indexdic[remaining]]
            indexdic[num]=i
        