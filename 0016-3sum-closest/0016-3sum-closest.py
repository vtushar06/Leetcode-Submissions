class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
    
        for i in range(n):
            left, right = i + 1, n - 1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                # If this sum is closer to target, update
                if abs(s - target) < abs(closest_sum - target):
                    closest_sum = s
                
                # Move pointers based on comparison
                if s == target:
                    return s
                elif s < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum