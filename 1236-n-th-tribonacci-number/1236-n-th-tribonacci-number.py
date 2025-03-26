class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 0:
        #     return 0
        # elif n == 1 or n == 2:
        #     return 1

        # trib = [0] * (n + 1)
        # trib[0], trib[1], trib[2] = 0, 1, 1

        # for i in range(3, n + 1):
        #     trib[i] = trib[i - 1] + trib[i - 2] + trib[i - 3]

        # return trib[n]
        dp={0:0,1:1,2:1}
        def find(n):
            if n<=0:
                return 0
            if n in dp:
                return dp[n]
            dp[n]=find(n-3)+find(n-2)+ find(n-1)
            return dp[n]
        return find(n)           
        