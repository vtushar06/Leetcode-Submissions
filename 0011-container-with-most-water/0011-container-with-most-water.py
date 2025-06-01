class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxarea=float("-inf")
        while(l<=r):
            length=r-l
            breath=min(height[l],height[r])
            maxarea=max(maxarea,(length*breath))
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxarea            
        