class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101
        
        # count frequency
        for n in nums:
            freq[n] += 1
        
        # prefix sum: freq[i] = how many numbers < i
        for i in range(1, 101):
            freq[i] += freq[i - 1]
        
        # build answer
        ans = []
        for n in nums:
            if n == 0:
                ans.append(0)
            else:
                ans.append(freq[n - 1])
        
        return ans