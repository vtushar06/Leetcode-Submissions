class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexdic={}
        for i,num in enumerate(nums):
            remaining=target-num
            if remaining in indexdic.keys():
                return[i,indexdic[remaining]]
            indexdic[num]=i