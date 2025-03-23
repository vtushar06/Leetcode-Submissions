class Solution(object):
    def minCostClimbingStairs(self, cost):
        memo={}
        def findcost(costs,n,index):
            if n==1:
                return costs[0]
            if index in memo:
                return memo[index]
            if index==n-1 or index==n-2:
                return costs[index]
            else:
                jump1=costs[index]+findcost(costs,n,index+1)
                jump2=costs[index]+findcost(costs,n,index+2)
                memo[index]=min(jump1,jump2)
                return memo[index]
        return min(findcost(cost,len(cost),0),findcost(cost,len(cost),1))            


        