class Solution(object):
    def diagonalPrime(self, nums):
        def isprime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if (n%i)==0:
                    return False
            return True 
        n=len(nums)
        largest=0
        for i in range(n):
            if (isprime(nums[i][i])):
                largest=max(largest,nums[i][i])
            if i !=n-1-i and isprime(nums[i][n-i-1]):
                largest=max(largest,nums[i][n-i-1]) 
        return largest if largest else 0         
                         
