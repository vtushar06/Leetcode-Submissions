class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i*i, n + 1, i):
                        is_prime[j] = False
            return is_prime
  

        def findprime(left,right):
            ans=[]
            isprimes=sieve(right)
            primearr=[i for i in range(left,right+1) if isprimes[i]]
            minabsolutediff=float("inf")
            for i in range(len(primearr)-1):
                absdiff=abs(primearr[i]-primearr[i+1])
                if absdiff<minabsolutediff:
                    minabsolutediff=absdiff
                    ans=[primearr[i],primearr[i+1]]
            if ans:
                return ans
            else:
                return [-1,-1]    
        return findprime(left,right)
        